from fastapi import FastAPI
import uvicorn

app = FastAPI(title="FastAPI Docker App", version="0.1.0")


@app.get("/")
async def root():
    return {"message": "Hello from fastapi-docker!"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}


@app.get("/favicon.ico")
async def favicon():
    return {"message": "No favicon"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
