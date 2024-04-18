# FastAPIBackend

## Instruction
1. clone this repo by ```git clone https://github.com/runjiezhao1/FastAPIBackend.git```<br />
2. use ```pip install``` to download and install the required packages<br />
3. If you want to run the server, please execute the command ```uvicorn main:app --reload --port 5000```. If you wan to run the tests, please execute the command ```pytest```

## Comments
1. Postman and sqlite studio can better help you to understand what happens if you create, delete or select the task.

## Code Structure
| -- .gitignore <br />
| -- README.md <br />
| -- database.py <br />
| -- main.py <br />
| -- models.py <br />
| -- schemas.py <br />
| -- sql_app.db <br />
| -- test_main.py <br />

## DDL for tables
EventEntity table: <br />
create table EventEntity( <br />
    id integer primary key autoincrement, <br />
    title varchar(255) not null, <br />
    description varchar(255), <br />
    status varchar(255) check(status in ('TODO','IN_PROGRESS','COMPLETED')), <br />
    createdAt DATE, <br />
    updatedAt DATE, <br />
    startTime varchar(5) not null check  (startTime REGEXP '[0-9]{2}:[0-9]{2}'), <br />
    endTime varchar(5) not null check  (endTime REGEXP '[0-9]{2}:[0-9]{2}') <br />
) <br />

UsersEntity table: <br />
create table UsersEntity(<br />
    id int NOT NULL,<br />
    name varchar(255),<br />
    primary key(id)<br />
)<br />

EventUsers table: <br />
create table EventUsers( <br />
    eventId int NOT NULL, <br />
    userId int NOT NULL, <br />
    FOREIGN KEY(eventId) references EventEntity(id), <br />
    FOREIGN KEY(userId) references UsersEntity(id) <br />
)