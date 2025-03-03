from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database.db_config import SessionLocal, engine
from database.models import Manager
import bcrypt

app = FastAPI()

# Dependency: Get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# create manager API
@app.post("/create_manager/")
def create_manager(username: str, email: str, password: str, db: Session = Depends(get_db)):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    new_manager = Manager(username=username, email=email, password_hash=hashed_password)

    db.add(new_manager)
    db.commit()
    return {"message": "✅ Manager created successfully!"}


# Login API
@app.post("/login/")
def login_manager(email: str, password: str, db: Session = Depends(get_db)):
    # Finding a user in the database
    manager = db.query(Manager).filter(Manager.email == email).first()

    if not manager:
        raise HTTPException(status_code=400, detail="❌ User does not exist!")

    # Verify Password
    if not bcrypt.checkpw(password.encode('utf-8'), manager.password_hash.encode('utf-8')):
        raise HTTPException(status_code=400, detail="❌ Wrong password!")

    return {"message": "✅ Login successful"}
