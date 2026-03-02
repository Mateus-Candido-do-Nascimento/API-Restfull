from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException

app = FastAPI(
    title="task manager API",
    description="API para gerenciamento de tarefas",
    version="1.0.0"
)

class Task(BaseModel):
    title: str
    description: str
    completed: bool = False

class TaskResponse(Task):
    id: int

class MessageResponse(BaseModel):
    message: str

tasks = []

@app.get("/")
def welcome():
    return {"message": "Bem vindo a API"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/tasks", response_model=TaskResponse, status_code=201)
def create_task(task: Task):
    task_dict = task.dict()
    task_dict["id"] = len(tasks) + 1
    tasks.append(task_dict)
    return task_dict

@app.get("/tasks", response_model=list[TaskResponse], status_code=200)
def list_tasks(completed: Optional[bool] = None):
    if completed is None:
        return tasks
    return [task for task in tasks if task["completed"] == completed]

@app.get("/tasks/{task_id}", response_model=TaskResponse, status_code=200)
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="task nao encontrada")


@app.put("/tasks/{task_id}", response_model=TaskResponse, status_code=200)
def update_task(task_id: int, task_update: Task):
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = task_update.title
            task["description"] = task_update.description
            task["completed"] = task_update.completed
            return task
    raise HTTPException(status_code=404, detail="task nao encontrada")

@app.delete("/tasks/{task_id}", response_model=MessageResponse, status_code=200)
def delete_by_id(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return {"message": f"task {task_id} removida"}
    raise HTTPException(status_code=404, detail="task nao encontrada")