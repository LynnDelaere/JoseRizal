#Author:YIBO LIANG

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File,Form
from sqlalchemy.orm import Session
from backend.dependencies import get_db
from backend.auth import get_current_user
from database.models import City
from pydantic import BaseModel, HttpUrl
from typing import Optional
import os
import shutil

router = APIRouter()

class CityCreate(BaseModel):
    name: str
    description: str
    image_url: Optional[HttpUrl] = None

UPLOAD_DIR = "static/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/add_city/")
async def add_city(
    name: str = Form(...),
    description: str = Form(...),
    file: UploadFile = File(None),
    db: Session = Depends(get_db),
    current_admin = Depends(get_current_user)
):
    existing_city = db.query(City).filter(City.name == name).first()
    if existing_city:
        raise HTTPException(status_code=400, detail="❌ City already exists!")

    image_url = None
    if file:
        file_path = f"{UPLOAD_DIR}/{file.filename}"
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        image_url = f"/{file_path}"  

    new_city = City(
        name=name,
        description=description,
        image_url=image_url
    )
    db.add(new_city)
    db.commit()

    return {"message": f"✅ City '{name}' created successfully!", "image_url": image_url}


@router.get("/cities", response_model=list[dict])
def get_cities(db: Session = Depends(get_db)):
    cities = db.query(City).all()
    return [{"id": city.id, "name": city.name} for city in cities]


@router.delete("/delete_city/{city_id}")
def delete_city(
    city_id: int, 
    db: Session = Depends(get_db),
    current_admin = Depends(get_current_user)
):
    city = db.query(City).filter(City.id == city_id).first()
    if not city:
        raise HTTPException(status_code=404, detail="❌ City not found!")
    
    db.delete(city)
    db.commit()
    return {"message": f"✅ City '{city.name}' deleted successfully!"}



class CityUpdate(BaseModel):
    name: str
    description: str
    image_url: Optional[HttpUrl] = None


@router.put("/update_city/{city_id}")
def update_city(
    city_id: int, 
    city_data: CityUpdate, 
    db: Session = Depends(get_db),
    current_admin = Depends(get_current_user)
):
    city = db.query(City).filter(City.id == city_id).first()
    if not city:
        raise HTTPException(status_code=404, detail="❌ City not found!")
    
    # 更新字段
    city.name = city_data.name
    city.description = city_data.description
    if city_data.image_url is not None:  
        city.image_url = city_data.image_url
    db.commit()
    
    return {"message": f"✅ City '{city.name}' updated successfully!"}


@router.get("/city/{city_id}")
def get_city(city_id: int, db: Session = Depends(get_db)):
    city = db.query(City).filter(City.id == city_id).first()
    if not city:
        raise HTTPException(status_code=404, detail="❌ City not found!")
    
    return {
        "id": city.id,
        "name": city.name,
        "description": city.description,
        "image_url": city.image_url
    }
