## Overview
This repository contains a BERT-based sentiment analysis model fine-tuned on the Stanford IMDB dataset, along with a FastAPI service that exposes both JSON and HTML endpoints. You can:

- Train & evaluate the model locally with MLflow

- Serve the model via FastAPI and docker

- Dockerize the service and launch with a single docker-compose up

All Python dependencies are pinned to specific versions to avoid breakages caused by upstream updates.

## Prerequisites
- Git ≥ 2.20
- Python 3.9.x
- Docker ≥ 20.10
- Docker Compose plugin (v2)
- (Optional) virtualenv or conda for local Python environment
