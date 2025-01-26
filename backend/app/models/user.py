# backend/app/models/user.py

from sqlalchemy import Column, Integer, String
from app.database import Base  # Base, app/database.py'den alınacak

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    full_name = Column(String, nullable=True)
    # buralara normalizasyon yapılacak !!!
    english_level = Column(String, nullable=False, default="A1")
    purpose = Column(String, nullable=False, default="General")
    weakest_sections = Column(String, nullable=False, default="Speaking")
    time_period = Column(String, nullable=False, default="5")
    question_prompt = Column(String, nullable=True)