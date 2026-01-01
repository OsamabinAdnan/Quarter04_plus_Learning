from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr

app = FastAPI(
    title="For testing purpose",
    description="We are exploring FastAPI in class first time",
    version="1.0.0",
)


@app.get("/")
def main():
    return {
        "id": 1,
        "name": "Osama bin Adnan",
        "age": 26,
        "occupation": "Agentic AI Developer",
    }

# Path Parameters
@app.get("/users/{user_id}")
def get_user(user_id: int):
    """Get a specific user by their ID"""
    # user_id is extracted from the URL
    # GET /users/42 → user_id = 42
    # Above line means "Get the user with ID 42"
    return {"user_id": user_id, "name": "John"}

# Query Parameter
@app.get("/users/")
def get_users(
    skip: int = 0, # Default value = optional
    limit: int = 10, # Pagination
    active: bool = True # Filter
    ):
    """Get users with optional filtering"""
     # GET /users/?skip=0&limit=5&active=true
     # Above line means "Get the first 5 active users"
    return {
    "skip": skip,
    "limit": limit,
    "active_only": active
    }

# Combining Both Path and Query Parameters
@app.get("/users/{user_id}/posts")
def get_user_posts(
    user_id: int, # Path: required
    published: bool = True, # Query: optional
    limit: int = 10 # Query: optional
    ):
    # GET /users/42/posts?published=true&limit=5
    # Above line means "Get the user with ID 42 and return last 5 published posts"
    return {"user_id": user_id, "limit": limit}

# Pydantic Validation
class UserCreate(BaseModel):
    name: str = Field(..., min_length=2) # Field is required and min_length is 2
    email: EmailStr
    age: int = Field(..., ge=0, le=120) # Greater than or equal to 0 and less than or equal to 120

@app.post("/create_users/")
def create_user_good(user: UserCreate):
    return user # Already validated!