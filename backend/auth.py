#Author:YIBO LIANG

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
import jwt
from datetime import datetime, timedelta
from database.models import admin
from passlib.context import CryptContext
from backend.dependencies import get_db

# JWT 配置
SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Password hashing configuration
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

router = APIRouter()

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta if expires_delta else timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

@router.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    manager = db.query(admin).filter(
        (admin.username == form_data.username) | (admin.email == form_data.username)
    ).first()
    if not manager:
        raise HTTPException(status_code=400, detail="❌ 用户不存在，请检查用户名或邮箱！")
    if not pwd_context.verify(form_data.password, manager.password_hash):
        raise HTTPException(status_code=400, detail="❌ 密码错误，请重试！")
    access_token = create_access_token(
        data={"sub": manager.username, "email": manager.email},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": {
            "username": manager.username,
            "email": manager.email
        }
    }

async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="❌ 无效的令牌")
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="❌ 令牌已过期，请重新登录")
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="❌ 令牌无效")
    manager = db.query(admin).filter(admin.username == username).first()
    if not manager:
        raise HTTPException(status_code=401, detail="❌ 用户不存在")
    return manager
