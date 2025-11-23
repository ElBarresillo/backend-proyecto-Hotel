from fastapi import APIRouter
from app.db.supabase_client import supabase
from app.schemas.huespedes_schemas import Huesped

router = APIRouter(prefix="/huespedes", tags=["Huespedes"])

@router.get("/")
def listar_huespedes():
    return supabase.table("huespedes").select("*").execute().data

@router.post("/")
def crear_huesped(huesped: Huesped):
    return supabase.table("huespedes").insert(huesped.dict()).execute().data
