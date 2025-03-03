from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

# 从环境变量获取数据库配置
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
# 创建数据库引擎
engine = create_engine(DATABASE_URL)

# 创建 Session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)