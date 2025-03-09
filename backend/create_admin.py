#Author:YIBO LIANG

import bcrypt
from database.db_config import SessionLocal
from database.models import admin

print("🚀 create_admin.py is running!")  

def create_admin():
    db = SessionLocal()
    print("✅ Database session created!")  

    username = input("Enter admin username: ")
    email = input("Enter admin email: ")
    password = input("Enter password: ")

    # Hash the password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    # Create an administrator
    new_admin = admin(username=username, email=email, password_hash=hashed_password)

    db.add(new_admin)
    db.commit()
    print("✅ Admin created successfully!")

if __name__ == "__main__":
    print("🔍 Script started!")  
    create_admin()
