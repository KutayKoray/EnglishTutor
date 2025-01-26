# backend/app/init_db.py

from app.database import engine, Base
from app.models import User, Question

Base.metadata.create_all(bind=engine)
