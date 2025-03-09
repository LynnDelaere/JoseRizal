#Author:YIBO LIANG

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database.models import Location, LocationMedia, admin
from backend.dependencies import get_db
from backend.auth import get_current_user

router = APIRouter()

# Pydantic Model - for creating and updating LocationMedia
class LocationMediaCreate(BaseModel):
    location_id: int
    media_url: str
    media_type: str
    description: str = None

class LocationMediaUpdate(BaseModel):
    media_url: str
    media_type: str
    description: str = None

# 1. add LocationMedia
@router.post("/add_media/")
def add_media(
    media_data: LocationMediaCreate,
    db: Session = Depends(get_db),
    current_admin: admin = Depends(get_current_user)
):
    # Check if location_id is valid
    location = db.query(Location).filter(Location.id == media_data.location_id).first()
    if not location:
        raise HTTPException(status_code=404, detail="❌ Location not found!")

    new_media = LocationMedia(
        location_id=media_data.location_id,
        media_url=media_data.media_url,
        media_type=media_data.media_type,
        description=media_data.description
    )
    db.add(new_media)
    db.commit()
    db.refresh(new_media)

    return {"message": f"✅ Media added successfully to location ID {media_data.location_id}!", "id": new_media.id}

# 2. Get all media at the specified Location
@router.get("/location/{location_id}/media")
def get_location_media(location_id: int, db: Session = Depends(get_db)):
    media_list = db.query(LocationMedia).filter(LocationMedia.location_id == location_id).all()
    if not media_list:
        raise HTTPException(status_code=404, detail="❌ No media found for this location!")

    return [
        {
            "id": media.id,
            "location_id": media.location_id,
            "media_url": media.media_url,
            "media_type": media.media_type,
            "description": media.description,
            "created_at": media.created_at
        }
        for media in media_list
    ]

# 3. delet the specified Media
@router.delete("/delete_media/{media_id}")
def delete_media(
    media_id: int,
    db: Session = Depends(get_db),
    current_admin: admin = Depends(get_current_user)
):
    media = db.query(LocationMedia).filter(LocationMedia.id == media_id).first()
    if not media:
        raise HTTPException(status_code=404, detail="❌ Media not found!")

    db.delete(media)
    db.commit()
    return {"message": f"✅ Media ID {media_id} deleted successfully!"}

# 4. Update the specified Media
@router.put("/update_media/{media_id}")
def update_media(
    media_id: int,
    media_data: LocationMediaUpdate,
    db: Session = Depends(get_db),
    current_admin: admin = Depends(get_current_user)
):
    media = db.query(LocationMedia).filter(LocationMedia.id == media_id).first()
    if not media:
        raise HTTPException(status_code=404, detail="❌ Media not found!")

    media.media_url = media_data.media_url
    media.media_type = media_data.media_type
    media.description = media_data.description
    db.commit()

    return {"message": f"✅ Media ID {media_id} updated successfully!"}
