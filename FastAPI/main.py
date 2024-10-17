from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return "Hola mundo"

@app.get("/suma/{a}/{b}")
def suma(a: int, b: int):
    return a + b

