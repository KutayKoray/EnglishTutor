# backend/app/database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database URL (modify according to your database configuration)
DATABASE_URL = "sqlite:///./test.db"  # Example for SQLite, replace with your DB URL

# SQLAlchemy Engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# SQLAlchemy Session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
