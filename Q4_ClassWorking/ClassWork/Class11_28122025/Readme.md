# Class 11 Backend (cont.) - 28/12/2025

## FastAPI
- Revise last class topics
- If you do developers something good then learn `Abstraction`, which means make simple stuffs/things by hiding complications. FastAPI did the same things
- Behind the scene FastAPI is working on `Starlette`, it is a framework use to make async services.
- Starlette made framework but did not provide proper abstraction of it.
- The Python web framework FastAPI was created by **Sebastián Ramírez Montaño**, an open-source developer also known by his GitHub handle, **tiangolo**.
- He recently lanuched `FastAPI Cloud`, you can deploy FastAPI application at [FastAPI cloud](https://fastapicloud.com).

### 04 Creating Endpoints
- We have learned in last class 01 What is Backend?, 02 HTTP Basics, 03 FastAPI Setup.
- In this topic we will learn 04 Creating Endpoints.
    * GET, POST, PUT, DELETE + Path & Query Parameters

#### Path vs Query Parameters

---

![Path vs Query Parameters](assets/Path%20vs%20Query%20Parameters.png)

---
- Path is used to access the resource.
- **Purpose:** Path parameters are an essential part of the URL used to uniquely identify a specific resource or a hierarchy of resources.
- **Placement:** They are embedded directly in the URL path, often represented by placeholders like {id} or :id in the API definition.
- **Syntax:** In a live URL, the placeholders are replaced with actual values.
    * *Example:* https://api.example.com/users/123 where `123` is the `user ID`.
- **Requirement:** They are mandatory for the API endpoint to function correctly, as they define the location of the resource.
- **Best Use Cases:** Retrieving, updating, or deleting a specific item, such as a user account, a specific order, or a file within a specific folder. 
- **Caching:** Easier to cache (resource identifier)

```python
@app.get("/users/{user_id}")
def get_user(user_id: int):
    """Get a specific user by their ID"""
     # user_id is extracted from the URL
     # GET /users/42 → user_id = 42
    return {"user_id": user_id, "name": "John"}

```

![Path Parameter Example](assets/Path%20Parameter%20Example.png)

- Query is used to filter, sort, and paginate the resource.
- **Purpose:** Query parameters provide additional information to the server to refine the request, such as filtering data, sorting results, or implementing pagination.
- **Placement:** They are appended to the end of the URL after a question mark (?).
- **Syntax:** They are key-value pairs, with multiple parameters separated by an ampersand (&).
    * *Example:* https://api.example.com/users?status=active&sort=name where `status` and `sort` are query parameters.
- **Requirement:** They are generally optional, and if omitted, the API usually applies a default behavior.
- **Best Use Cases:** Searching, filtering lists of items, sorting results, or managing the number of items returned (e.g., limit, offset, page). 
- **Caching:** Caching is more complex (dependent on parameters)

```python
@app.get("/users/")
def get_users(
    skip: int = 0, # Default value = optional
    limit: int = 10, # Pagination
    active: bool = True # Filter
    ):
    """Get users with optional filtering"""
     # GET /users/?skip=0&limit=5&active=true
    return {
    "skip": skip,
    "limit": limit,
    "active_only": active
    }
```

![Query Parameter Example](assets/Query%20Parameter%20Example.png)


### 05 Pydantic Models & Validation
- In TypeScript, we used ZOD for data validation but in Python we use Pydantic.
- Pydantic automatically validates incoming data based on type hints, eliminating the need for manual
validation code and preventing bugs from invalid data.

```python
# ■ WITHOUT Pydantic (tedious & error-prone)

@app.post("/users/")
def create_user_bad(data: dict):
    if "name" not in data:
        raise HTTPException(400, "Name required")
    if not isinstance(data.get("age"), int):
        raise HTTPException(400, "Age must be int")
    # ... many more checks needed

# ■ WITH Pydantic (clean & automatic)

class UserCreate(BaseModel):
    name: str = Field(..., min_length=2)
    email: EmailStr
    age: int = Field(..., ge=0, le=120)

@app.post("/users/")
def create_user_good(user: UserCreate):
    return user # Already validated!
```
#### Complete Model Example

```python
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

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
```

#### Common Field Validators

| Validator   | Purpose                 | Example                                   |
|------------|--------------------------|-------------------------------------------|
| min_length | Min string length        | `Field(..., min_length=2)`                |
| max_length | Max string length        | `Field(..., max_length=100)`              |
| ge         | Greater or equal         | `Field(..., ge=0)`                        |
| le         | Less or equal            | `Field(..., le=150)`                      |
| gt / lt    | Greater / Less than      | `Field(..., gt=0)`                        |
| regex      | Pattern match            | `Field(..., pattern="^[a-z]+$")`          |

### 06 Complete CRUD API
Full Working Implementation with In-Memory Storage

#### In-Memory Storage

```python
# app/data/store.py
users_db: dict = {}
user_id_counter: int = 1

def get_next_id() -> int:
    global user_id_counter # The `global` keyword tells Python that the variable is **defined outside the function** and should be **modified globally**, not treated as a local variable.
    current = user_id_counter
    user_id_counter += 1
    return current
```

#### CREATE — POST /users/

```python
@app.post("/users/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate):
     # Check for duplicate email
    for existing in users_db.values():
        if existing["email"] == user.email:
            raise HTTPException(400, "Email exists")

    user_id = get_next_id()
    new_user = {
        "id": user_id,
        **user.model_dump(),
        "created_at": datetime.now(),
        "is_active": True
    }
    users_db[user_id] = new_user
    return new_user
```
Check complete code in [Complete CRUD API](/fastapi_learning/store.py)
