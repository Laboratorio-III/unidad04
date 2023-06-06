from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hola mundo"}

@app.get("/valor/{var}")
def valor(var):
    return {"valor": var}