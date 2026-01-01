from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field, EmailStr
from datetime import datetime
from typing import Optional, List

app = FastAPI()

# Complete Pydantic Model

class UserBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    age: Optional[int] = Field(None, ge=0, le=150)

class UserCreate(UserBase):
    password: str = Field(..., min_length=8)

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None

class UserResponse(UserBase):
    id: int
    created_at: datetime
    is_active: bool = True 



# In-Memory Storage
users_db: dict = {}
user_id_counter: int = 1

def get_next_id() -> int:
    global user_id_counter # The `global` keyword tells Python that the variable is **defined outside the function** and should be **modified globally**, not treated as a local variable.
    current = user_id_counter
    user_id_counter += 1
    return current

@app.get("/")
def main():
    return {
        "id": 1,
        "name": "Osama bin Adnan",
        "age": 26,
        "occupation": "Agentic AI Developer",
        "app": "This is store.py",
    }



# CREATE — POST /users/
@app.post("/users/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate):
     # Check for duplicate email
    for existing in users_db.values():
        if existing["email"] == user.email:
            raise HTTPException(400, "Email exists")

    user_id = get_next_id()
    new_user = {
        "id": user_id,
        **user.model_dump(), # ** unpacks the dictionary and it keyword arguments, and then it puts them  in a new dictionary in json format.
        "created_at": datetime.now(),
        "is_active": True
    }
    users_db[user_id] = new_user
    return new_user

# READ — GET /users/ and GET /users/{id}
@app.get("/users/", response_model=List[UserResponse])
def get_all_users(skip: int = 0, limit: int = 100):
    users = list(users_db.values())
    return users[skip : skip + limit]

@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(
            status_code=404,
            detail=f"User {user_id} not found"
        )
    return users_db[user_id]

# UPDATE — PUT /users/{id}
@app.put("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user_update: UserUpdate):
    if user_id not in users_db:
        raise HTTPException(404, "User not found")
    stored_user = users_db[user_id]
    update_data = user_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        stored_user[field] = value
    return stored_user 

# DELETE — DELETE /users/{id}

@app.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(404, "User not found")
    del users_db[user_id]
    return None # 204 = No Content 