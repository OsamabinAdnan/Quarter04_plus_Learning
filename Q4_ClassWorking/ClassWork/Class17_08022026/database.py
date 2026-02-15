from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
import os

load_dotenv()

database_url = os.getenv("NEON_DATABASE_URL")
if not database_url:
    raise ValueError("NEON_DATABASE_URL not found in environment variables")

engine = create_engine(database_url, echo=True)

# Create database and tables if not exists
def create_db_and_tables():
    """Create all tables in the database."""
    SQLModel.metadata.create_all(engine)

# Dependency that provides database sessions
def get_session():
    """Dependency that provides database sessions."""
    with Session(engine) as session:
        yield session
        # yield is used to hold the session for the duration of the request
