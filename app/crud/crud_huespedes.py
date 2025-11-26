from app.db.supabase_client import supabase
from app.schemas.huespedes_schemas import Huesped

def obtenerTodosHuespedes():
    return supabase.table("huespedes").select("*").execute().data

def obtenerHuespedId(id: int):
    data = supabase.table("huespedes").select("*").eq("id", id).execute().data
    return data[0] if data else None

def obtenerHuespedEmail(email: str):
    return supabase.table("huespedes").select("*").eq("email", email).execute().data

def obtenerHuespedPhone(phone: str):
    return supabase.table("huespedes").select("*").eq("phone", phone).execute().data

def crearHuesped(huesped: Huesped):
    return supabase.table("huespedes").insert(huesped.dict()).execute().data

def updateHuesped(id: int, huesped: Huesped):
    return supabase.table("huespedes").update(huesped.dict()).eq("id", id).execute().data

def deleteHuesped(id: int):
    return supabase.table("huespedes").delete().eq("id", id).execute().data