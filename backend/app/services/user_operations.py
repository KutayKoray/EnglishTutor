# backend/app/services/user_operations.py

from sqlalchemy.orm import Session
from app.models.user import User
from passlib.context import CryptContext
import jwt
import datetime

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = "your_secret_key"  # Replace with a secure secret key

def create_user(db: Session, username: str, email: str, password: str, english_level: str, purpose: str, weakest_sections: str, time_period: str):
    if db.query(User).filter(User.email == email).first() or db.query(User).filter(User.username == username).first():
        return False  # User already exists
    hashed_password = pwd_context.hash(password)
    new_user = User(
        username=username, 
        email=email, 
        hashed_password=hashed_password, 
        english_level=english_level, 
        purpose=purpose, 
        weakest_sections=weakest_sections, 
        time_period=time_period
        )
    db.add(new_user)
    db.commit()
    return True

def authenticate_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()
    if user and pwd_context.verify(password, user.hashed_password):
        token = jwt.encode(
            {"user_id": user.id, "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=24)},
            SECRET_KEY,
            algorithm="HS256",
        )
        return token
    return None
