#Author:YIBO LIANG
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.dependencies import get_db
from backend.auth import get_current_user
from database.models import City
from pydantic import BaseModel
router = APIRouter()

class CityCreate(BaseModel):
    name: str
    description: str

@router.post("/add_city/")
def add_city(
    city_data: CityCreate, 
    db: Session = Depends(get_db),
    current_admin = Depends(get_current_user)
):
    existing_city = db.query(City).filter(City.name == city_data.name).first()
    if existing_city:
        raise HTTPException(status_code=400, detail="❌ City already exists!")
    new_city = City(name=city_data.name, description=city_data.description)
    db.add(new_city)
    db.commit()
    return {"message": f"✅ City '{city_data.name}' created successfully!"}
