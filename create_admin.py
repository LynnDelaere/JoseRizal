import bcrypt
from database.db_config import SessionLocal
from database.models import Manager

print("🚀 create_admin.py is running!")  # 添加调试信息

def create_admin():
    db = SessionLocal()
    print("✅ Database session created!")  # 添加调试信息

    username = input("Enter admin username: ")
    email = input("Enter admin email: ")
    password = input("Enter password: ")

    # 哈希加密密码
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    # 创建管理员
    new_admin = Manager(username=username, email=email, password_hash=hashed_password)

    db.add(new_admin)
    db.commit()
    print("✅ Admin created successfully!")

if __name__ == "__main__":
    print("🔍 Script started!")  # 添加调试信息
    create_admin()
