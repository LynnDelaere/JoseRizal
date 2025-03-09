#Author:YIBO LIANG

# dependencies.py
from database.db_config import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
