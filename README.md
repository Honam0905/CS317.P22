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
