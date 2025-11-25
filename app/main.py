from fastapi import FastAPI
from app.api import cuartos_api, huespedes_api, reservaciones_api, pagos_api, cargos_api
from app.api import cuartos_api, huespedes_api, reservaciones_api
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Hotel API")
app.include_router(cuartos_api.router)
app.include_router(huespedes_api.router)
app.include_router(reservaciones_api.router)
app.include_router(pagos_api.router)
app.include_router(cargos_api.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],  
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos (GET, POST, PUT, DELETE)
    allow_headers=["*"],  # Permitir todos los encabezados
)

# Endpoint raiz
@app.get("/")
def read_root():
    return {"message": "Bienvenido, jala a la perfeccion"}
