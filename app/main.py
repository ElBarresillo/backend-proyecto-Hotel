from fastapi import FastAPI
from app.api import cuartos_api, huespedes_api, reservaciones_api, pagos_api, cargos_api, auth_api
from fastapi.middleware.cors import CORSMiddleware

tags_metadata = [
    {
        "name": "Auth",
        "description": "Operaciones de autenticación y gestión de usuarios."
    },
    {
        "name": "Cuartos",
        "description": "Gestión de habitaciones del hotel."
    },
    {
        "name": "Huespedes",
        "description": "Gestión de huéspedes registrados."
    },
    {
        "name": "Reservaciones",
        "description": "Gestión de reservaciones de habitaciones."
    },
    {
        "name": "Pagos",
        "description": "Gestión de pagos realizados por los huéspedes."
    },
    {
        "name": "Cargos",
        "description": "Gestión de cargos extra realizados a los huéspedes."
    }
]

app = FastAPI(
    title="Hotel API",
    description="API para la gestión de un hotel: habitaciones, huéspedes, reservaciones, pagos y cargos.",
    version="1.0.0",
    openapi_tags=tags_metadata
)

app.include_router(cuartos_api.router)
app.include_router(huespedes_api.router)
app.include_router(reservaciones_api.router)
app.include_router(pagos_api.router)
app.include_router(cargos_api.router)
app.include_router(auth_api.router)

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
