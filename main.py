"""
API-Learning-Lab — Phase 1: API Fundamentals (básico)

Request journey so far: Client → HTTP → Uvicorn → FastAPI → Code → Response
Visto hasta ahora: GET, POST básico, path params, query params (concepto)
Pendiente: Body JSON, Pydantic, list/dict storage (Session 06)
"""

from fastapi import FastAPI

app = FastAPI()


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


# POST básico — visto como concepto (sin body/Pydantic aún, se verá en S06)
@app.post("/items/")
def crear_item():
    return {"mensaje": "POST recibido — body se verá en Session 06"}

