# SQL model for object-relational mapping (ORM)
# Serve as a data model for database and Pydantic model for data validation
from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime


class Task(SQLModel, table=True):
    """Task stored in database."""
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(min_length=1, max_length=200)
    description: Optional[str] = None
    status: str = Field(default="pending")
    created_at: datetime = Field(default_factory=datetime.now)

# table=True - This model maps to a database table
# primary_key=True - Auto-incrementing ID
# Field(default=...) - Column defaults
# Optional[int] = None - ID is None until database assigns it