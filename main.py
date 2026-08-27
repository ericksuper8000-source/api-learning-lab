'''
Cliente -> HTTP -> Uvicorn -> FastApi -> Pydantic -> Codigo -> Base de datos >

La sintaxis de Query Parameters en FastAPI
La regla es siempre la misma:
def mi_funcion(parametro_normal: tipo, parametro_query: tipo = valor_por_defecto):
- Sin valor por defecto → es un parámetro normal (obligatorio)
- Con valor por defecto → FastAPI lo detecta como query parameter automáticamente
Ejemplos claros
# query parameter de tipo string, opcional (puede ser None)
def read_items(q: str | None = None):

# query parameter de tipo boolean, opcional (default False)
def read_item(item_id: int, verbose: bool = False):

# query parameter de tipo string, opcional (default "corto")
def read_item(item_id: int, formato: str = "corto"):
No hay decorador especial. No hay Query() a menos que quieras validaciones avanzadas. Solo es el parámetro con su valor por defecto.

'''

from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

# Esto define lo que el cliente debe enviar, si no lo manda asi da un error 422
class Item(BaseModel):
    name : str
    brand : str
    serial : str
    status : str = "active"

@app.get('/')
def root():
    return {
        'Mensaje': "Hello World"
    }

@app.get('/hello')
def say_hello():
    return {
        'Mensaje': "Hola desde /hello"
    }

@app.get('/items/')
def read_items(
        q: str | None = None
):
    if q:
        return {'filtrado_por': q}
    return {'mensaje': "No se envio el filtro"}

items = []

@app.get('/items/lista')
def listar_items():
    return items

@app.get('/items/{item_id}')
def read_item(
        item_id: int,
        verbose: bool = False,
        formato: str = "normal"
):
    if formato == "corto":
        return {"item_id": item_id}

    if formato == "largo":
        return {
            "item_id": item_id,
            "tipo": "camino",
            "estado": "activo",
            "ubicacion": "oficina 3"
        }

    if verbose:
        return {
            "item_id": item_id,
            "tipo": "camino",
            "detalle": "Información completa del item"
        }

    return {"item_id": item_id}

@app.post('/items/', status_code=201)
def crear_item(
        item : Item
):
    items.append(item.model_dump())
    return item
