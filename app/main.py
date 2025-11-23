
from fastapi import FastAPI
from app.api import cuartos_api, huespedes_api

app = FastAPI()
app.include_router(cuartos_api.router)
app.include_router(huespedes_api.router)
