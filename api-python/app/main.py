from fastapi import FastAPI
from pydantic import BaseModel
 
app = FastAPI(
    title="task manager API",
    description="API para gerenciamento de tarefas",
    version="1.0.0"
)

class Task(BaseModel):
    title: str
    description: str
    completed: bool = False

@app.post("/tasks")
def create_task(task: Task):
    return {
        "messsage" : "Tarefa criada com sucesso",
        "task": task
    }


@app.get("/health")
def health_check():
    return {"status" : "ok"} 
     
@app.get("/")
def welcome():
    return { "message" : "Bem vindo a API"}

@app.get("/task/{task_id}")
def get_task(task_id:int):
    return {
        "task_id": task_id,
        "title": "estudar fastapi",
        "completed": False
    }

@app.get("/tasks")
def list_tasks(completed: bool | None = None):
    return{
        "filter_completed": completed
    }