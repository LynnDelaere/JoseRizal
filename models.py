
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, DECIMAL, Interval
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import bcrypt
from sqlalchemy.dialects.postgresql import JSONB

# 创建基类
Base = declarative_base()

# 初始化 SQLAlchemy（假设使用 Flask-SQLAlchemy）
#db = SQLAlchemy()

# 1. 城市表 (cities)
class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text)

    # 关系
    locations = relationship("Location", back_populates="city")
    routes = relationship("Route", back_populates="city")

# 2. 地点表 (locations)
class Location(Base):
    __tablename__ = 'locations'
    id = Column(Integer, primary_key=True, autoincrement=True)
    city_id = Column(Integer, ForeignKey('cities.id'), nullable=False)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    location_data = Column(JSONB, nullable=False)  # JSONB 存储位置信息
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    # reletion
    city = relationship("City", back_populates="locations")
    media = relationship("LocationMedia", back_populates="location")
    route_locations = relationship("RouteLocation", back_populates="location")

# 3. 地点媒体表 (location_media)
class LocationMedia(Base):
    __tablename__ = 'location_media'
    id = Column(Integer, primary_key=True, autoincrement=True)
    location_id = Column(Integer, ForeignKey('locations.id'), nullable=False)
    media_url = Column(Text, nullable=False)
    media_type = Column(String(50))
    description = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # 关系
    location = relationship("Location", back_populates="media")

# 4. 路线表 (routes)
class Route(Base):
    __tablename__ = 'routes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    city_id = Column(Integer, ForeignKey('cities.id'), nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(Text)
    estimated_time = Column(Interval)
    status = Column(String(20), default='draft')
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    # 关系
    city = relationship("City", back_populates="routes")
    route_locations = relationship("RouteLocation", back_populates="route")

# 5. 路线与地点关联表 (route_locations)
class RouteLocation(Base):
    __tablename__ = 'route_locations'
    id = Column(Integer, primary_key=True, autoincrement=True)
    route_id = Column(Integer, ForeignKey('routes.id'), nullable=False)
    location_id = Column(Integer, ForeignKey('locations.id'), nullable=False)
    sequence_order = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # 关系
    route = relationship("Route", back_populates="route_locations")
    location = relationship("Location", back_populates="route_locations")

# 6. CMS内容表 (cms_content)
class CMSContent(Base):
    __tablename__ = 'cms_content'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    body = Column(Text, nullable=False)
    language = Column(String(10), default='en')
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

# 7. 后台管理员用户表 (users)
class Manager(Base):
    __tablename__ = 'managers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)  # 存储哈希后的密码
    email = Column(String(255), unique=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    # 1. 生成哈希密码
    @staticmethod
    def hash_password(plain_password):
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(plain_password.encode('utf-8'), salt).decode('utf-8')

    # 2. 校验密码
    def verify_password(self, plain_password):
        return bcrypt.checkpw(plain_password.encode('utf-8'), self.password_hash.encode('utf-8'))