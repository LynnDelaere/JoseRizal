from db_config import engine
from models import Base

# 创建数据库表
def init_db():
    try:
        Base.metadata.create_all(engine)
        print("✅ The database table was created successfully!")
    except Exception as e:
        print(f"❌ Failed to create database table: {e}")

if __name__ == "__main__":
    init_db()
