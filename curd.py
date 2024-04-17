from sqlalchemy.orm import Session
from models import User, Item, Temp
from schemas import UserCreate, ItemCreate, TempCreate


# 根据 id 获取 user
def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


# 根据 email 获取 user
def get_user_by_email(db: Session, id: str):
    return db.query(User).filter(User.id == id).first()


# 获取所有 user
def get_users(db: Session, size: int = 0, limit: int = 100):
    return db.query(User).offset(size).limit(limit).all()

def get_names(db: Session, size: int = 0, limit: int = 100):
    return db.query(Temp).offset(size).limit(limit).all()

def create_names(db: Session):
    tempCreator = Temp(id=3, name="hello")
    db.add(tempCreator)
    db.commit
    # db.refresh(tempCreator)
    db.flush()
    return tempCreator

# 创建 user，user 类型是 Pydantic Model
def create_user(db: Session, user: UserCreate):
    fake_hashed_password = user.password + "superpolo"
    # 1、使用传进来的数据创建 SQLAlchemy Model 实例对象
    db_user = User(email=user.email, hashed_password=fake_hashed_password)
    # 2、将实例对象添加到数据库会话 Session 中
    db.add(db_user)
    # 3、将更改提交到数据库
    db.commit()
    # 4、刷新实例，方便它包含来自数据库的任何新数据，比如生成的 ID
    db.refresh(db_user)
    return db_user


# 获取所有 item
def get_items(db: Session, size: int = 0, limit: int = 100):
    return db.query(Item).offset(size).limit(limit).all()


# 创建 item，item 类型是 Pydantic Model
def create_item(db: Session, item: ItemCreate, user_id: int):
    db_item = Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item