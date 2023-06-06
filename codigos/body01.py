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