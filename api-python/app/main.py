from fastapi import FastAPI
 
app = FastAPI(
    title="task manager API",
    description="API para gerenciamento de tarefas",
    version="1.0.0"
)

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