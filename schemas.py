from typing import List, Optional

from pydantic import BaseModel


# Item 的基类,表示创建和查询 Item 时共有的属性
class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None


# 创建 Item 时的 Model
class ItemCreate(ItemBase):
    pass


# 查询 Item 时的 Model
class Item(ItemBase):
    id: int
    owner_id: int

    # 向 Pydantic 提供配置
    class Config:
        #  orm_mode 会告诉 Pydantic 模型读取数据，即使它不是字典，而是 ORM 模型（或任何其他具有属性的任意对象）
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True

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