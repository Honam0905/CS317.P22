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
1. Cài Git LFS (chỉ làm 1 lần trên máy)
    Lý do vì file mô hình .pt được up lên bằng việc sử dụng git lfs nên trong đoạn code sẽ gặp vấn đề nếu không dùng command git lfs trước
   ```bash
   git lfs install
   ```
2. Clone repo:
   
   ```bash
   git clone https://github.com/Honam0905/CS317.P22.git
   cd CS317.P22
   ```
3. Kéo file nhị phân
   ```bash
   git lfs fetch --all
   git lfs checkout
   ```
4. Tạo và kích hoạt virtualenv( Nếu cần thiết)
   
   ```bash
   python3.9 -m venv venv
   source venv/bin/activate
   ```
5. Cài đặt dependencies
   
   ```bash
   pip install --upgrade pip
   pip install --no-cache-dir -r serve/requirements.txt
   ```
6. Chạy FastAPI (Local)
   
   ```bash
   cd serve
   uvicorn app:app --host 0.0.0.0 --port 8000
   ```
   Sau khi thành công mở các đường link ở mục 8.1
7. Đóng gói & Deploy với Docker<br>
   ```bash
   cd CS317.P22/bert_sentiment_analysis
   ```
   7.1. Ở thư mục gốc, build image:
   
   ```bash
   docker compose build sentiment-api
   ```
   7.2. Khởi chạy container:
   
   ```bash
   docker compose up -d
   ```
   7.3. Kiểm tra trạng thái:
   
   ```bash
   docker ps
   ```
   7.4. Kiểm tra lỗi nếu có:

   ```bash
   docker logs <container-name>/<container-id>
   ```

   * Lưu ý khi chạy xong câu lệnh 7.2 khi bấm vào đường link 8.1 sẽ hiện ra lỗi phải mất một lúc thì mới kết nối được nên khi chạy xong 7.2 chờ đợi một lúc để local host nhận được tín hiệu trừ trường hợp mạng mạnh
9. Gọi API

   8.1. Qua trình duyệt  
      - HTML form: http://localhost:8000/  
      - Swagger UI:  http://localhost:8000/docs  

   8.2. Sử dụng Curl

      ```bash
      curl -X POST "http://localhost:8000/predict" \
           -H "Content-Type: application/json" \
           -d '{"text":"I loved this movie!"}'
      ```

   6.3. Kết quả trả về

      ```json
      {"label":"positive","score":0.9876}
      ```
