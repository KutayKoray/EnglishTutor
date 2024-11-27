# backend/app/api/auth.py

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.database import get_db
from app.models.user import User
from app.services.user_operations import create_user, authenticate_user

router = APIRouter()

# Request models
class UserRegister(BaseModel):
    username: str
    email: str
    password: str
    english_level: str
    purpose: str
    weakest_sections: str
    time_period: str

class UserLogin(BaseModel):
    email: str
    password: str

@router.post("/register")
def register_user(user: UserRegister, db: Session = Depends(get_db)):
    if create_user(db, user.username, user.email, user.password, user.english_level, user.purpose, user.weakest_sections, user.time_period):
        return {"message": "User registered successfully"}
    raise HTTPException(status_code=400, detail="User already exists")

@router.post("/login")
def login_user(user: UserLogin, db: Session = Depends(get_db)):
    token = authenticate_user(db, user.email, user.password)
    if token:
        return {"token": token}
    raise HTTPException(status_code=401, detail="Invalid email or password")
