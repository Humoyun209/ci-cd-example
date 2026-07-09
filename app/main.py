from fastapi import FastAPI, HTTPException
from fastapi import status
from pydantic import BaseModel

app = FastAPI(title="Simple Todo API")

todos = [
    {"id": 1, "title": "Изучить CI/CD", "completed": False},
    {"id": 2, "title": "Настроить GitHub Actions", "completed": False},
]


class TodoCreate(BaseModel):
    title: str


@app.get("/todos")
def get_todos():
    return todos


@app.post("/todos", status_code=status.HTTP_201_CREATED)
def create_todo(todo: TodoCreate):
    new_todo = {"id": len(todos) + 1, "title": todo.title, "completed": False}
    todos.append(new_todo)
    return new_todo


@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for todo in todos:
        if todo["id"] == todo_id:
            todos.remove(todo)
            return {"message": "Task deleted"}
    raise HTTPException(status_code=404, detail="Todo not found")
