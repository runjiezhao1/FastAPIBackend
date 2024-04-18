from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base

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