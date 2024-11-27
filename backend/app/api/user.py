# backend/app/api/user.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import User

router = APIRouter()

@router.get("/profile")
def get_user_profile(user_id: int, db: Session = Depends(SessionLocal)):
    user = db.query(User).filter(User.id == user_id).first()
    return user
