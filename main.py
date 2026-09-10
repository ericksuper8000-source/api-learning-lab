"""
API-Learning-Lab — Phase 1: API Fundamentals (básico)

Request journey so far: Client → HTTP → Uvicorn → FastAPI → Pydantic → Code → Response
Visto: GET, POST + Body + Pydantic, path, query, caja/lista + 201/422 (S06 real 2026-09-10)
Siguiente: S06 refuerzo (Ej1 location, Ej2 assigned_to) → S07
"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name : str
    brand : str
    serial : str
    status : str = 'active'

caja : list[dict] = []

# POST con Pydantic + 201 — S06 real (Body validado, guarda fotocopia en caja)
@app.post("/items/", status_code=201)
def crear_item(
        item : Item
):
    caja.append(item.model_dump())
    return item

@app.get('/items/lista')
def listar_items():
    return caja

@app.get("/")
def root():
    return {"Mensaje": "Hello World"}


@app.get("/hello")
def say_hello():
    return {"Mensaje": "Hola desde /hello"}


# Path param básico — {item_id} es variable en la URL
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}


# Query param básico — ?q=... es filtro opcional
@app.get("/items/")
def read_items(q: str | None = None):
    if q:
        return {"filtrado_por": q}
    return {"mensaje": "No se envio el filtro"}