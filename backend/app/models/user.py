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
    english_level = Column(String, nullable=False, default="A1") # A1, A2, B1, B2, C1, C2
    purpose = Column(String, nullable=False, default="General") # General, Academic, Business, Exam Preparation
    weakest_sections = Column(String, nullable=False, default="Speaking") # Listening, Reading, Writing, Speaking
    time_period = Column(String, nullable=False, default="5") # 5, 10, 15, 20, 25, 30
    question_prompt = Column(String, nullable=True) # burası her ai api isteği yapıldığınca kullanılacak promptun başı burası kullanıcının seviyesi amacı ve weakest sectionsına göre değişecek bunu hesaplayan bir fonksiyon buraya o bilgileri kayıttan sonra kaydedicek.
