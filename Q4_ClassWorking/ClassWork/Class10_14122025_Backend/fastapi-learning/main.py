from fastapi import FastAPI

app = FastAPI(
    title="For testing purpose",
    description="We are exploring FastAPI in class first time",
    version="1.0.0",
    
)

@app.get("/")
def main():
    return {
        "id": 1,
        "name":"Osama bin Adnan",
        "age": 26,
        "occupation":"Agentic AI Developer",
    }

