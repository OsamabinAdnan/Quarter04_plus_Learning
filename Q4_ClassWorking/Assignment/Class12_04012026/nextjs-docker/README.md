# Next.js Docker Application

This is a [Next.js](https://nextjs.org) project bootstrapped with [`create-next-app`](https://nextjs.org/docs/app/api-reference/cli/create-next-app) and containerized with Docker for easy deployment and scaling.

## Features

- Modern Next.js 15 application using the App Router
- Docker containerization for consistent deployments
- Optimized for performance and scalability
- Ready for cloud deployment

## Getting Started

### Running with Docker (Recommended)

```bash
# Build and start the application with Docker Compose
docker-compose up --build

# Access the application at http://localhost:3000
```

### Alternative: Running with Docker Commands

```bash
# Build the Docker image
docker build -t nextjs-docker .

# Run the container
docker run -p 3000:3000 nextjs-docker

# Access the application at http://localhost:3000
```

### Development Mode (without Docker)

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js) - your feedback and contributions are welcome!

## Docker Configuration

This project includes:
- `Dockerfile` - Multi-stage build configuration for production-ready container
- `docker-compose.yml` - Service configuration for easy local development
- `.dockerignore` - Specifies files to exclude from Docker build context

## Deploy on Vercel or with Docker

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Alternatively, you can deploy using Docker to any container orchestration platform such as:
- AWS ECS
- Google Cloud Run
- Azure Container Instances
- Kubernetes clusters
- DigitalOcean App Platform
