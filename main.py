from fastapi import FastAPI, Depends, HTTPException, status, Path, Query, Body
from database import SessionLocal, engine
from sqlalchemy.orm import Session
import schemas
from models import Temp, EventEntity, EventUsers
from schemas import User, UserCreate, ItemCreate, Item, TempCreate, EventEntityCreate
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

#create new tasks
@app.post("/tasks")
async def create_task(data: EventEntityCreate, db: Session = Depends(get_db)):
    try:
        newEventEntity = EventEntity(title=data.title, description=data.description, 
                                    status=data.status, createdAt=data.createdAt, updatedAt=data.updatedAt,
                                    startTime=data.startTime, endTime=data.endTime)
        db.add(newEventEntity)
        db.commit()
        db.refresh(newEventEntity)
    except:
        return {"message":"Cannot add new task. Please check your input json"}
    for i in data.userId:
        try:
            newEventUsers = EventUsers(eventId=newEventEntity.id, userId=i)
            db.add(newEventUsers)
            db.commit()
            db.refresh(newEventUsers)
        except:
            return {"message":"Cannot add new related users to this task. Please check your input json"}
    return {"message":"add tasks success"}

#get task by id
@app.get("/task/{task_id}")
async def get_task(task_id: int, db: Session = Depends(get_db)):
    try:
        result = db.query(EventEntity).filter(EventEntity.id == task_id).first()
    except:
        return {"message":"Cannot get the task with specified id. Please check your input"}
    return result

#remove task by id
@app.post("/remove_task/{task_id}")
async def remove_task(task_id: int, db: Session = Depends(get_db)):
    eventUsers = db.query(EventUsers).filter(EventUsers.eventId == task_id).all()
    for i in eventUsers:
        db.delete(i)
        db.commit()
    task = db.query(EventEntity).filter(EventEntity.id == task_id).all()
    for i in task:
        db.delete(i)
        db.commit()
    return {"message":"delete successful"}

def sortFunc(e):
    return e['startTime']

@app.get("/merge_event/{user_id}")
async def merge_event(user_id: int, db : Session = Depends(get_db)):
    eventUsers = db.query(EventUsers).filter(EventUsers.userId == user_id).all()
    events = []
    for i in eventUsers:
        relatedEvent = db.query(EventEntity).filter(EventEntity.id == i.eventId).first()
        events.append({"startTime":relatedEvent.startTime,"endTime":relatedEvent.endTime})
    events.sort(key=sortFunc)
    if len(events) <= 1:
        return events
    i = 0
    while i < len(events) - 1:
        if events[i]['endTime'] > events[i+1]['startTime']:
            events[i]['endTime'] = events[i+1]['endTime']
            del events[i+1]
            continue
        i = i + 1
    return events