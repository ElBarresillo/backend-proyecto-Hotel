from fastapi import APIRouter
from app.db.supabase_client import supabase
from app.schemas.cuartos_schemas import Cuarto

router = APIRouter(prefix="/cuartos", tags=["Cuartos"])

#Obtener todos los cuartos
@router.get("/")
def listar_cuartos():
    return supabase.table("cuartos").select("*").execute().data

#Obtener un cuarto
@router.get("/{id}")
def obtener_cuarto(id: int):
    return supabase.table("cuartos").select("*").eq("id", id).execute().data

#Crea un cuarto
@router.post("/")
def crear_cuarto(cuarto: Cuarto):
    return supabase.table("cuartos").insert(cuarto.dict()).execute().data

#Actualiza un cuarto existente
@router.put("/{id}")
def actualizar_cuarto(id: int, cuarto: Cuarto):
    return supabase.table("cuartos").update(cuarto.dict()).eq("id", id).execute().data

#Elimina un cuarto
@router.delete("/{id}")
def eliminar_cuarto(id: int):
    return supabase.table("cuartos").delete().eq("id", id).execute().data