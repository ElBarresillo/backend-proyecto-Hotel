from app.db.supabase_client import supabase

def obtenerReservaciones():
    return supabase.table("reservaciones").select("*").execute().data

def obtenerReservacionesID(id: int):
    data = supabase.table("reservaciones").select("*").eq("id", id).execute().data
    return data[0] if data else None

def obtenerReservacionPorCuarto(room_id: int):
    return supabase.table("reservaciones").select("*").eq("room_id", room_id).execute().data

def crearReservacion(data: dict):
    return supabase.table("reservaciones").insert(data).execute().data[0]

def updateEstadoReservacion(id: int, status: str):
    return supabase.table("reservaciones").update({"status": status}).eq("id", id).execute().data

def deleteReservacion(id: int):
    return supabase.table("reservaciones").delete().eq("id", id).execute().data