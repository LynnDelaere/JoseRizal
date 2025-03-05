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
