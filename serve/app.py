from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import torch, os, glob, re
from transformers import BertTokenizerFast, BertForSequenceClassification
from torch.nn.functional import softmax

class TextIn(BaseModel):
    text: str

class PredictionOut(BaseModel):
    label: str
    score: float

def find_best_ckpt(output_dir="output"):
    pattern = os.path.join(output_dir, "bert_epoch*.pt")
    files = glob.glob(pattern)
    if not files:
        raise FileNotFoundError(f"No checkpoints found in {output_dir}")
    def epoch_num(fn):
        m = re.search(r"bert_epoch(\d+)\.pt$", fn)
        return int(m.group(1)) if m else -1
    return max(files, key=epoch_num)

# Load model & tokenizer
CKPT = find_best_ckpt("output")
PRETRAINED = "bert-base-uncased"
NUM_LABELS = 2

tokenizer = BertTokenizerFast.from_pretrained(PRETRAINED)
model = BertForSequenceClassification.from_pretrained(PRETRAINED, num_labels=NUM_LABELS)
state = torch.load(CKPT, map_location="cpu")
model.load_state_dict(state)
model.eval()

app = FastAPI(title="BERT Sentiment API")

# HTML form at root
@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <html>
      <head>
        <title>Sentiment Analyzer</title>
      </head>
      <body>
        <h1>Enter text for Sentiment Analysis</h1>
        <form action="/analyze" method="post">
          <textarea name="text" rows="4" cols="60" placeholder="Type your text here..."></textarea><br>
          <button type="submit">Analyze</button>
        </form>
      </body>
    </html>
    """

# Form handler
@app.post("/analyze", response_class=HTMLResponse)
async def analyze(text: str = Form(...)):
    # Tokenize & predict
    inputs = tokenizer(
        text,
        truncation=True,
        padding="max_length",
        max_length=128,
        return_tensors="pt"
    )
    with torch.no_grad():
        logits = model(**inputs).logits
        probs  = softmax(logits, dim=-1)[0]
        idx    = int(probs.argmax())
        label  = "positive" if idx == 1 else "negative"
        score  = probs[idx].item()

    # Return result in HTML
    return f"""
    <html>
      <head><title>Result</title></head>
      <body>
        <h1>Sentiment Analysis Result</h1>
        <p><strong>Text:</strong> {text}</p>
        <p><strong>Sentiment:</strong> {label}</p>
        <p><strong>Confidence:</strong> {score:.4f}</p>
        <a href="/">Analyze another text</a>
      </body>
    </html>
    """

# (Optional) keep the original JSON API
@app.post("/predict", response_model=PredictionOut)
def predict(payload: TextIn):
    inputs = tokenizer(
        payload.text,
        truncation=True,
        padding="max_length",
        max_length=128,
        return_tensors="pt"
    )
    with torch.no_grad():
        logits = model(**inputs).logits
        probs  = softmax(logits, dim=-1)[0]
        idx    = int(probs.argmax())
        label  = "positive" if idx == 1 else "negative"
        return PredictionOut(label=label, score=float(probs[idx]))
