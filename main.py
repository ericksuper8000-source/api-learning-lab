from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def root():
    return {
        'Mensaje' : "Hello World"
    }

@app.get('/hello')
def say_hello():
    return {
        'Mensaje' : "Hola desde /hello"
    }

@app.get('/items/{item_id}')
def read_item(
        item_id : int
):
    return {
        "item_id" : item_id,
        'tipo' : "camino"
    }