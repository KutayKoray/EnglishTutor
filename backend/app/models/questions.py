# backend/app/models/question.py

from sqlalchemy import Column, Integer, String
from app.database import Base

class Question(Base):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True, index=True)
    question_text = Column(String)
    correct_answer = Column(String)
    explanation = Column(String)
