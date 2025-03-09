
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, DECIMAL, Interval
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import bcrypt
from sqlalchemy.dialects.postgresql import JSONB

# Creating a Base Class
Base = declarative_base()



# 1. (cities)
class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text)
    image_url = Column(Text , nullable=True)

    # relation
    locations = relationship("Location", back_populates="city")
    routes = relationship("Route", back_populates="city")

# 2. (locations)
class Location(Base):
    __tablename__ = 'locations'
    id = Column(Integer, primary_key=True, autoincrement=True)
    city_id = Column(Integer, ForeignKey('cities.id'), nullable=False)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    location_data = Column(JSONB, nullable=False)  # JSONB Storing location information
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    # reletion
    city = relationship("City", back_populates="locations")
    media = relationship("LocationMedia", back_populates="location")
    route_locations = relationship("RouteLocation", back_populates="location")

# 3. (location_media)
class LocationMedia(Base):
    __tablename__ = 'location_media'
    id = Column(Integer, primary_key=True, autoincrement=True)
    location_id = Column(Integer, ForeignKey('locations.id'), nullable=False)
    media_url = Column(Text, nullable=False)
    media_type = Column(String(50))
    description = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # relation
    location = relationship("Location", back_populates="media")

# 4. (routes)
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

    # reletion
    city = relationship("City", back_populates="routes")
    route_locations = relationship("RouteLocation", back_populates="route")

# 5.  (route_locations)
class RouteLocation(Base):
    __tablename__ = 'route_locations'
    id = Column(Integer, primary_key=True, autoincrement=True)
    route_id = Column(Integer, ForeignKey('routes.id'), nullable=False)
    location_id = Column(Integer, ForeignKey('locations.id'), nullable=False)
    sequence_order = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # relation
    route = relationship("Route", back_populates="route_locations")
    location = relationship("Location", back_populates="route_locations")

# 6. CMS Table of Content (cms_content)
class CMSContent(Base):
    __tablename__ = 'cms_content'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    body = Column(Text, nullable=False)
    language = Column(String(10), default='en')
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

# 7. Backstage administrator user table (users) 
class admin(Base):
    __tablename__ = 'admin'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)  # 存储哈希后的密码
    email = Column(String(255), unique=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    # 1. Generate hashed password
    @staticmethod
    def hash_password(plain_password):
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(plain_password.encode('utf-8'), salt).decode('utf-8')

    # 2. Verify password
    def verify_password(self, plain_password):
        return bcrypt.checkpw(plain_password.encode('utf-8'), self.password_hash.encode('utf-8'))