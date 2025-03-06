from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

# Get database configuration from environment variables
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
# Creating a database engine
engine = create_engine(DATABASE_URL)

# Creating a Session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
