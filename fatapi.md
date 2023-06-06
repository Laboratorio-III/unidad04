# FastAPI
## ¿Qué es FastAPI?

FastAPI es un framework web moderno, rápido y rápido para Python. Fue desarrollado para proporcionar un alto rendimiento, fácil de usar, fácil de aprender y fácil de escalar. Con FastAPI, los desarrolladores pueden crear APIs RESTful de alto rendimiento utilizando Python 3.7+.

## ¿Por qué usar FastAPI?

* Rápido: FastAPI está diseñado para ser rápido, con tiempos de respuesta de menos de 1 ms.
* Fácil de usar: FastAPI es fácil de aprender y fácil de usar, incluso para desarrolladores nuevos en Python.
* Fácil de escalar: FastAPI se integra fácilmente con otros marcos y herramientas de Python para escalar aplicaciones.

## Instalación
`pip install fastapi`

`pip install "uvicorn[standard]"`


## Código de ejemplo
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hola mundo"}
```
`uvicorn main:app --reload`

## Parámetros tipo path

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hola mundo"}

@app.get("/valor/{var}")
def valor(val):
    return {"valor": var}

```
## Parámetros path con tipo
```py
@app.get("/valor/{var}")
def valor(val: int):
    return {"valor": var}
```
## Parámetros de query

```py
@app.get("/sum")
def valor(sum1: int, sum2: int):
    return {"sum": sum1 + sum2}
```

## Parámetros opcionales

```py
from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get("/sumo")
def sumo(sum1: Union[int, None]  = 0, sum2: Union[int, None] = 0): 
    return {"sumo": sum1 + sum2}

```

## Request body
```py
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    nombre: str
    descripcion: Union[str, None] = None
    fecha: Union[str, None] = None

app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    return item
```