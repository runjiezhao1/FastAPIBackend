from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello123"}

def test_merge():
    response = client.get("/merge_event/1")
    assert response.status_code == 200
    assert response.json() == {"result":[
        {
            "startTime": "02:02",
            "endTime": "03:34"
        },
        {
            "startTime": "04:00",
            "endTime": "05:00"
        }
    ]}

def test_create_tasks():
    response = client.post("/tasks/",
                          json={
                            "title":"Testcase",
                            "description":"describe",
                            "status": "COMPLETED",
                            "createdAt": "2024-04-18 19:38:10",
                            "updatedAt": "2024-04-18 19:38:10",
                            "startTime": "04:00",
                            "endTime": "05:00",
                            "userId": [1,2]
                          })
    assert response.status_code == 200
    assert response.json() == {"message":"add tasks success"}

def test_delete_tasks():
    response = client.post("/remove_task/1")
    assert response.status_code == 200
    assert response.json() == {"message":"delete successful"}

def test_get_task():
    response = client.get("/task/2")
    assert response.status_code == 200
    assert response.json() == {
        "title": "Test",
        "description": "describe",
        "createdAt": "2024-04-18 19:38:10",
        "startTime": "02:02",
        "status": "TODO",
        "id": 2,
        "updatedAt": "2024-04-18 19:38:10",
        "endTime": "03:01"
    }

def test_create_tasks_fail():
    response = client.post("/tasks/",
                          json={
                            "title":"Testcase",
                            "description":"describe",
                            "status": "NOT TODO",
                            "createdAt": "2024-04-18 19:38:10",
                            "updatedAt": "2024-04-18 19:38:10",
                            "startTime": "04:00",
                            "endTime": "05:00",
                            "userId": [1,2]
                          })
    assert response.status_code == 200
    assert response.json() == {"message":"Cannot add new task. Please check your input json"}

def test_get_task():
    response = client.get("/task/23")
    assert response.status_code == 200
    assert response.json() == {
        "title": "Testcase",
        "description": "describe",
        "createdAt": "2024-04-18 19:38:10",
        "startTime": "04:00",
        "status": "COMPLETED",
        "id": 23,
        "updatedAt": "2024-04-18 19:38:10",
        "endTime": "05:00"
    }