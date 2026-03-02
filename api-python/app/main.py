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
    
tasks = []

@app.post("/tasks")
def create_task(task: Task):
    task_dict = task.dict()
    task_dict["id"] = len(tasks)+1
    tasks.append(task_dict)
    return {
        "message" : "Tarefa criada com sucesso",
        "task": task_dict
    }
    
@app.delete("/tasks/{task_id}")
def delete_by_id(task_id: int):
    for task in tasks:
        if task["id"]==task_id:
            tasks.remove(task)
            return {"message": f"task {task_id} removida"}
    raise HTTPException(status_code=404, detail="task nao encontrada") 
    

@app.put("/tasks/{task_id}")
def update_task(task_id: int, task_update: Task):
    for task in tasks:
        if task["id"]==task_id:
            task["title"]= task_update.title
            task["description"]= task_update.description
            task["completed"] = task_update.completed
            return{"message ":"task atualizada ","task": task}
    raise HTTPException(status_code=404, detail="task nao encontrada")
        


@app.get("/health")
def health_check():
    return {"status" : "ok"} 
     
@app.get("/")
def welcome():
    return { "message" : "Bem vindo a API"}

@app.get("/tasks/{task_id}")
def get_task(task_id:int):
    for task in tasks:
        if task["id"]==task_id:
            return task
    raise HTTPException(status_code=404, detail= "task nao encontrada")
    
@app.get("/tasks")
def list_tasks_completed(completed: Optional[bool] = None):
    if completed is None:
        return tasks
    return [task for task in tasks if task["completed"] == completed]
