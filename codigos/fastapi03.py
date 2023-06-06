from fastapi import FastAPI
from typing import Union

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hola mundo"}

@app.get("/valor/{var}")
def valor(var: int):
    return {"valor": var}

@app.get("/sum")
def valor(sum1: int, sum2: int):
    return {"sum": sum1 + sum2}

@app.get("/sumo")
def sumo(sum1: Union[int, None]  = 0, sum2: Union[int, None] = 0): 
    return {"sumo": sum1 + sum2}