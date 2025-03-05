from db_config import engine
from models import Base

# 创建数据库表
def init_db():
    try:
        Base.metadata.create_all(engine)
        print("✅ 数据库表创建成功！")
    except Exception as e:
        print(f"❌ 数据库表创建失败: {e}")

if __name__ == "__main__":
    init_db()