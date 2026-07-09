from fastapi.testclient import TestClient
from fastapi import status
from .main import app

client = TestClient(app)


def test_get_todos():
    response = client.get("/todos")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 2


def test_create_todo():
    response = client.post("/todos", json={"title": "Купить молоко"})
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()["title"] == "Купить молоко"
    assert response.json()["id"] == 3


def test_delete_todo_success():
    response = client.delete("/todos/1")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "Task deleted"}


def test_delete_todo_not_found():
    response = client.delete("/todos/999")
    assert response.status_code == status.HTTP_404_NOT_FOUND
