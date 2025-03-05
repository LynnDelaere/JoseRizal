from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.auth import router as auth_router
from backend.admin_routes import router as admin_router
from backend.city_routes import router as city_router
from backend.location_routes import router as location_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Aggregate routes of various modules
app.include_router(auth_router, prefix="/auth")
app.include_router(admin_router)
app.include_router(city_router)
app.include_router(location_router)
