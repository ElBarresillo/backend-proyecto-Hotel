from app.db.supabase_client import supabase
from app.schemas.cuartos_schemas import Cuarto

def obtenerTodosCuartos():
    return supabase.table("cuartos").select("*").execute().data

def obtenerCuartoId(id: int):
    data = supabase.table("cuartos").select("*").eq("id", id).execute().data
    return data[0] if data else None

def obtenerCuartoNumero(number: str):
    return supabase.table("cuartos").select("*").eq("number", number).execute().data

def crearCuarto(cuarto: Cuarto):
    return supabase.table("cuartos").insert(cuarto.dict()).execute().data

def updateCuarto(id: int, cuarto: Cuarto):
    return supabase.table("cuartos").update(cuarto.dict()).eq("id", id).execute().data

def updateCuartoEstado(id: int, status: str):
    return supabase.table("cuartos").update({"status": status}).eq("id", id).execute().data

def deleteCuarto(id: int):
    return supabase.table("cuartos").delete().eq("id", id).execute().data