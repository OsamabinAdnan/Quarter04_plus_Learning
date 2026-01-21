# Containerized Projects Repository

This repository contains two simple containerized applications built with modern technologies:

1. **Next.js Docker Project** - A modern Next.js 15 application using the App Router
2. **FastAPI Docker Project** - A lightweight FastAPI application

Both projects are containerized with Docker for easy deployment and consistent environments.

## Projects Overview

### Next.js Docker Project
- **Technology**: Next.js 15 with TypeScript
- **Framework**: App Router
- **Container**: Docker with multi-stage build
- **Port**: 3000
- **Features**: Modern React application with optimized performance

### FastAPI Docker Project
- **Technology**: FastAPI with Python 3.13
- **Framework**: FastAPI web framework
- **Container**: Docker with slim Python image
- **Port**: 8000
- **Features**: RESTful API with health check endpoints

## Repository Structure

```
├── nextjs-docker/          # Next.js application with Docker
│   ├── app/               # Next.js app directory
│   ├── Dockerfile         # Docker configuration for Next.js
│   ├── package.json       # Node.js dependencies
│   └── README.md          # Next.js project documentation
├── fastapi-docker/       # FastAPI application with Docker
│   ├── main.py           # FastAPI application entry point
│   ├── Dockerfile        # Docker configuration for FastAPI
│   ├── pyproject.toml    # Python dependencies
│   └── README.md         # FastAPI project documentation
├── output-images/        # Docker Desktop screenshots
│   ├── docker-desktop-container.png    # Docker containers view
│   ├── docker-desktop-images.png       # Docker images view
│   ├── docker-image-building-nextjs.png # Next.js build process
│   ├── docker-image-building-fastapi.png # FastAPI build process
│   ├── nextjs-localhost3000.png       # Next.js running app
│   └── fastapi-localhost8000.png      # FastAPI running app
└── README.md             # This file (repository overview)
```

## Docker Desktop Screenshots

The `output-images/` directory contains screenshots showing:

1. **Docker Desktop Containers View** - Shows running containers for both applications
2. **Docker Desktop Images View** - Displays built Docker images
3. **Next.js Image Building** - Terminal output during Next.js Docker build
4. **FastAPI Image Building** - Terminal output during FastAPI Docker build
5. **Next.js Running** - Browser view of Next.js app at localhost:3000
6. **FastAPI Running** - Browser view of FastAPI app at localhost:8000

## Setup Instructions

### Prerequisites
- Docker Desktop installed and running
- Git for cloning the repository

### Running the Next.js Application

1. Navigate to the Next.js project directory:
   ```bash
   cd nextjs-docker
   ```

2. Build and run the Docker container:
   ```bash
   docker build -t nextjs-docker .
   docker run -p 3000:3000 nextjs-docker
   ```

3. Open your browser and visit `http://localhost:3000`

Alternative with Docker Compose (if docker-compose.yml is created):
   ```bash
   docker-compose up --build
   ```

### Running the FastAPI Application

1. Navigate to the FastAPI project directory:
   ```bash
   cd fastapi-docker
   ```

2. Build and run the Docker container:
   ```bash
   docker build -t fastapi-docker-app .
   docker run -p 8000:8000 fastapi-docker-app
   ```

3. Open your browser and visit `http://localhost:8000`

Alternative with Docker Compose (if docker-compose.yml is created):
   ```bash
   docker-compose up --build
   ```

## Key Features

### Next.js Project Features
- Modern Next.js 15 application using the App Router
- TypeScript support
- Multi-stage Docker build for optimized production image
- ESLint and PostCSS configurations
- Production-ready build process

### FastAPI Project Features
- FastAPI web framework with automatic API documentation
- Health check endpoint at `/health`
- Proper favicon handling to prevent 404 errors
- Dependency management with uv package manager
- Lightweight Python 3.13 slim image

## Docker Configuration Details

### Next.js Dockerfile
- Uses Node.js 22 Alpine image
- Multi-stage build process
- Installs dependencies and builds the application
- Exposes port 3000
- Runs the production build

### FastAPI Dockerfile
- Uses Python 3.13 slim image
- Copies project files to working directory
- Installs uv package manager
- Syncs dependencies from lock file
- Exposes port 8000
- Runs the FastAPI application

## Endpoints

### Next.js Application
- `http://localhost:3000` - Main application page

### FastAPI Application
- `http://localhost:8000` - Root endpoint returning welcome message
- `http://localhost:8000/health` - Health check endpoint
- `http://localhost:8000/favicon.ico` - Favicon endpoint

## Benefits of Containerization

1. **Consistent Environments**: Both applications run identically across different machines
2. **Easy Deployment**: Simply build and run the Docker images
3. **Dependency Isolation**: Each application has its own isolated environment
4. **Scalability**: Easy to scale applications with container orchestration
5. **Version Control**: Docker images can be versioned and managed like code

## Troubleshooting

### Common Issues
- Ensure Docker Desktop is running before building images
- Check that ports 3000 and 8000 are available
- Verify sufficient disk space for Docker images
- Make sure you're in the correct project directory

### Viewing Logs
To view container logs:
```bash
docker logs <container_name_or_id>
```

### Stopping Containers
To stop running containers:
```bash
docker stop <container_name_or_id>
```

## Technologies Used

- **Next.js 15**: React framework for production
- **FastAPI**: Modern, fast web framework for Python
- **TypeScript**: Typed JavaScript superset
- **Python 3.13**: Latest Python version
- **Docker**: Containerization platform
- **Node.js 22**: JavaScript runtime
- **uv**: Fast Python package installer and resolver