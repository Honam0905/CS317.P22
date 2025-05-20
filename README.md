## Overview
Dự án này cung cấp mô hình phân tích sentiment (positive/negative) sử dụng mô hình BERT được finetune trên tập Stanford IMDB dataset. Sử dụng FASTAPI và docker để deploy service

- Huấn luyện và đánh giá mô hình bằng MLflow

- Serve mô hình thông qua FastAPI và Docker

- đóng gói Docker, deploy với một lệnh `docker-compose up`

## Yêu cầu 
- Git ≥ 2.20
- Python 3.9.x
- Docker ≥ 20.10
- Docker Compose plugin (v2)
- (Optional) virtualenv or conda for local Python environment

## Cài đặt môi trường Python (Local)
1. Clone repo:
   
   ```bash
   git clone https://github.com/Honam0905/CS317.P22.git
   cd CS317.P22/bert_sentiment_analysis
   ```
2. Tạo và kích hoạt virtualenv( Nếu cần thiết)
   
   ```bash
   python3.9 -m venv venv
   source venv/bin/activate
   ```
3. Cài đặt dependencies
   
   ```bash
   pip install --upgrade pip
   pip install --no-cache-dir -r serve/requirements.txt
   ```
4. Chạy FastAPI (Local)
   
   ```bash
   cd serve
   uvicorn app:app --host 0.0.0.0 --port 8000
   ```
5. Đóng gói & Deploy với Docker<br>

   5.1. Ở thư mục gốc, build image:
   
   ```bash
   docker compose build sentiment-api
   ```
   5.2. Khởi chạy container:
   
   ```bash
   docker compose up -d
   ```
   5.3. Kiểm tra trạng thái:
   
   ```bash
   docker ps
   ```
6. Gọi API

   6.1. Qua trình duyệt  
      - HTML form: http://localhost:8000/  
      - Swagger UI:  http://localhost:8000/docs  

   6.2. Sử dụng Curl

      ```bash
      curl -X POST "http://localhost:8000/predict" \
           -H "Content-Type: application/json" \
           -d '{"text":"I loved this movie!"}'
      ```

   6.3. Kết quả trả về

      ```json
      {"label":"positive","score":0.9876}
      ```
