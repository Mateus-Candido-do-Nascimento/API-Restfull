from fastapi import FastAPI
 
app = FastAPI()

@app.get("/health")
def health_check():
    return {"status" : "ok"} 
     
@app.get("/")
def welcome():
    return { "message" : "Bem vindo a API"}

