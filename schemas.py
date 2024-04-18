from typing import List, Optional

from pydantic import BaseModel

class TempOutput(BaseModel):
    id: int
    name: str

class TempCreate(BaseModel):
    name: str

class EventEntityCreate(BaseModel):
    title: str
    description: str
    status: str
    createdAt: str
    updatedAt: str
    startTime: str
    endTime: str
    userId: List[int] = []

class EventUsersCreate(BaseModel):
    eventId: int
    userId: int

class UsersEntity(BaseModel):
    id: int
    name: str