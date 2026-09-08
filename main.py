"""
API-Learning-Lab — Phase 1: API Fundamentals

Request journey: Client → HTTP → Uvicorn → FastAPI → Pydantic → Code → Response

Query params rule in FastAPI:
    def func(path_param: type, query_param: type = default):
    - without default → path / required param
    - with default    → query param (FastAPI auto-detects)

No Query() needed unless you want extra validation (min_length, gt, etc.).
"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# In-memory store — will be replaced by PostgreSQL in Phase 3 (ADR-0006)
items: list[dict] = []


class Item(BaseModel):
    """Payload for POST /items/ — Pydantic validates before the function runs (422 on failure)."""

    name: str
    brand: str
    serial: str
    status: str = "active"


@app.get("/")
def root() -> dict[str, str]:
    return {"Mensaje": "Hello World"}


@app.get("/hello")
def say_hello() -> dict[str, str]:
    return {"Mensaje": "Hola desde /hello"}


@app.get("/items/")
def read_items(q: str | None = None) -> dict[str, str]:
    if q:
        return {"filtrado_por": q}
    return {"mensaje": "No se envio el filtro"}


@app.get("/items/lista")
def listar_items() -> list[dict]:
    return items


@app.get("/items/{item_id}")
def read_item(
    item_id: int,
    verbose: bool = False,
    formato: str = "normal",
) -> dict:
    if formato == "corto":
        return {"item_id": item_id}

    if formato == "largo":
        return {
            "item_id": item_id,
            "tipo": "camino",
            "estado": "activo",
            "ubicacion": "oficina 3",
        }

    if verbose:
        return {
            "item_id": item_id,
            "tipo": "camino",
            "detalle": "Información completa del item",
        }

    return {"item_id": item_id}


@app.post("/items/", status_code=201)
def crear_item(item: Item) -> Item:
    items.append(item.model_dump())
    return item
