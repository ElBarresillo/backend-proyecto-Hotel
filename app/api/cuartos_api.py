from fastapi import APIRouter
from app.db.supabase_client import supabase
from app.schemas.cuartos_schemas import Cuarto

router = APIRouter(prefix="/cuartos", tags=["Cuartos"])

@router.get("/")
def listar_cuartos():
    return supabase.table("cuartos").select("*").execute().data

@router.post("/")
def crear_cuarto(cuarto: Cuarto):
    return supabase.table("cuartos").insert(cuarto.dict()).execute().data
