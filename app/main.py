from fastapi import FastAPI
from app.api import cuartos_api, huespedes_api

app = FastAPI(title="Hotel API")
app.include_router(cuartos_api.router)
app.include_router(huespedes_api.router)

# Endpoint raiz
@app.get("/")
def read_root():
    return {"message": "Bienvenido, jala a la perfeccion"}
