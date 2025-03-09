#Author:YIBO LIANG
# backend/location_routes.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database.models import City, Location, admin
from backend.dependencies import get_db
from backend.auth import get_current_user

router = APIRouter()

# Define a Pydantic model to receive the request data for adding attractions
class LocationCreate(BaseModel):
    city_id: int
    name: str
    description: str
    location_data: dict

@router.post("/add_location/")
def add_location(
    location_info: LocationCreate,  # Parsing JSON data from the request body
    db: Session = Depends(get_db),
    current_admin: admin = Depends(get_current_user)
):
    # Check if the target city exists
    city = db.query(City).filter(City.id == location_info.city_id).first()
    if not city:
        raise HTTPException(status_code=404, detail="❌ City not found!")

    # Create a new attraction record
    new_location = Location(
        city_id=location_info.city_id,
        name=location_info.name,
        description=location_info.description,
        location_data=location_info.location_data
    )
    db.add(new_location)
    db.commit()
    return {"message": f"✅ Location '{location_info.name}' added to city ID {location_info.city_id} successfully!"}


@router.get("/city/{city_id}/locations", response_model=list[dict])
def get_locations_by_city(city_id: int, db: Session = Depends(get_db)):
    locations = db.query(Location).filter(Location.city_id == city_id).all()
    return [
        {
            "id": loc.id,
            "city_id": loc.city_id,
            "name": loc.name,
            "description": loc.description,
            "location_data": loc.location_data
        }
        for loc in locations
    ]



@router.get("/location/{location_id}")
def get_location(location_id: int, db: Session = Depends(get_db)):
    location = db.query(Location).filter(Location.id == location_id).first()
    if not location:
        raise HTTPException(status_code=404, detail="❌ Location not found!")

    return {
        "id": location.id,
        "city_id": location.city_id,
        "name": location.name,
        "description": location.description,
        "location_data": location.location_data
    }


@router.delete("/delete_location/{location_id}")
def delete_location(
    location_id: int,
    db: Session = Depends(get_db),
    current_admin: admin = Depends(get_current_user)
):
    location = db.query(Location).filter(Location.id == location_id).first()
    if not location:
        raise HTTPException(status_code=404, detail="❌ Location not found!")

    db.delete(location)
    db.commit()
    return {"message": f"✅ Location '{location.name}' deleted successfully!"}


class LocationUpdate(BaseModel):
    name: str
    description: str
    location_data: dict

@router.put("/update_location/{location_id}")
def update_location(
    location_id: int,
    location_data: LocationUpdate,
    db: Session = Depends(get_db),
    current_admin: admin = Depends(get_current_user)
):
    location = db.query(Location).filter(Location.id == location_id).first()
    if not location:
        raise HTTPException(status_code=404, detail="❌ Location not found!")

    location.name = location_data.name
    location.description = location_data.description
    location.location_data = location_data.location_data
    db.commit()

    return {"message": f"✅ Location '{location.name}' updated successfully!"}
