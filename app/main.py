from fastapi import FastAPI
from app.api import cuartos_api, huespedes_api, reservaciones_api, pagos_api, cargos_api, auth_api
app = FastAPI(title="Hotel API")
app.include_router(cuartos_api.router)
app.include_router(huespedes_api.router)
app.include_router(reservaciones_api.router)
app.include_router(pagos_api.router)
app.include_router(cargos_api.router)
app.include_router(auth_api.router)

# Endpoint raiz
@app.get("/")
def read_root():
    return {"message": "Bienvenido, jala a la perfeccion"}
