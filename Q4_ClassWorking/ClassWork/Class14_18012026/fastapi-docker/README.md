# FastAPI Docker App

This is a simple FastAPI application that has been containerized with Docker.

## Features

- FastAPI web framework
- Health check endpoint
- Favicon handling to prevent 404 errors
- Docker containerization
- Docker Compose support

## Setup Instructions

### Prerequisites

- Docker
- Docker Compose

### Running with Docker

1. Build the Docker image:
```bash
docker build -t fastapi-docker-app .
```

2. Run the container:
```bash
docker run -p 8000:8000 fastapi-docker-app
```

### Running with Docker Compose

1. Run the application:
```bash
docker-compose up
```

2. To run in detached mode:
```bash
docker-compose up -d
```

3. To stop the application:
```bash
docker-compose down
```

## Endpoints

- `GET /` - Root endpoint returning a welcome message
- `GET /health` - Health check endpoint
- `GET /favicon.ico` - Favicon endpoint (returns empty response to prevent 404 errors)

## Local Development

If you want to run the application locally without Docker:

1. Install dependencies:
```bash
pip install -e .
```

2. Run the application:
```bash
python main.py
```