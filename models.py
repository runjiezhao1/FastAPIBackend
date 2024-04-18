from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    # 1、表名
    __tablename__ = "users"

    # 2、类属性，每一个都代表数据表中的一列
    # Column 就是列的意思
    # Integer、String、Boolean 就是数据表中，列的类型
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")

class Temp(Base):
    __tablename__ = "temp"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)

class EventEntity(Base):
    __tablename__ = "EventEntity"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    status = Column(String, index=True)
    createdAt = Column(String, index=True)
    updatedAt = Column(String, index=True)
    startTime = Column(String, index=True)
    endTime = Column(String, index=True)

class UsersEntity(Base):
    __tablename__ = "UsersEntity"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, index=True)

class EventUsers(Base):
    __tablename__ = "EventUsers"

    eventId = Column(Integer, ForeignKey("EventEntity.id"), primary_key=True)
    userId = Column(Integer, ForeignKey("UsersEntity.id"), primary_key=True)