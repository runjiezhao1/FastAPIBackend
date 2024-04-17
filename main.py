from fastapi import FastAPI, Depends, HTTPException, status, Path, Query, Body
from database import SessionLocal, engine
from sqlalchemy.orm import Session
import schemas
from models import Temp
from schemas import User, UserCreate, ItemCreate, Item, TempCreate
import curd
import sys
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message" : "Hello123"}

# 创建用户
# @app.post("/users", response_model=User)
# async def create_user(user: UserCreate, db: Session = Depends(get_db)):
#     # 1、先查询用户是否有存在
#     db_user = curd.get_user_by_email(db, user.email)
#     if db_user:
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="user 已存在")
#     res_user = curd.create_user(db, user)
#     return res_user

# 根据 user_id 获取用户
@app.get("/user/{user_name}",response_model=list[schemas.TempOutput])
async def get_user(user_name: str, db: Session = Depends(get_db)):
    #return {"message" : "user_name"}
    return curd.get_names(db)

@app.post("/users")
async def create_user(user: TempCreate, db: Session = Depends(get_db)):
    newTemp = Temp(name=user.name)
    db.add(newTemp)
    db.commit()
    db.refresh(newTemp)
    #curd.create_names(db)
    return newTemp