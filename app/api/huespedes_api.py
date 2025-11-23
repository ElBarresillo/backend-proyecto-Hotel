from fastapi import APIRouter
from app.db.supabase_client import supabase
from app.schemas.huespedes_schemas import Huesped

router = APIRouter(prefix="/huespedes", tags=["Huespedes"])

#Obtengo todos los Huespedes
@router.get("/")
def listar_huespedes():
    return supabase.table("huespedes").select("*").execute().data

#Crea un huesped
@router.post("/")
def crear_huesped(huesped: Huesped):
    return supabase.table("huespedes").insert(huesped.dict()).execute().data

#Obtengo un solo huesped por id
@router.get("/{id}")
def obtener_huesped(id: int):
    return supabase.table("huespedes").select("*").eq("id", id).execute().data

#Actualiza un huesped por id
@router.put("/{id}")
def actualizar_huesped(id: int, huesped: Huesped):
    return supabase.table("huespedes").update(huesped.dict()).eq("id", id).execute().data

#Elimina un huesped por id
@router.delete("/{id}")
def eliminar_huesped(id: int):
    return supabase.table("huespedes").delete().eq("id", id).execute().data
