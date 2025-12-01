# app/crud/crud_pagos.py
from datetime import date
from app.db.supabase_client import supabase
from app.schemas.pagos_schemas import PagoCreate, PagoUpdate

SELECT_JOIN = """
    *,
    reservaciones (
        *,
        huespedes (name)
    )
"""

def obtenerTodosPagos():
    resp = supabase.table("pagos").select(SELECT_JOIN).order("id", desc=True).execute()
    return resp.data or []

def obtenerPagoId(id: int):
    resp = supabase.table("pagos").select(SELECT_JOIN).eq("id", id).limit(1).execute()
    data = resp.data or []
    return data[0] if data else None

def crearPago(pago: dict):
    # Asegurar formato de date
    if isinstance(pago.get("date"), date):
        pago["date"] = pago["date"].isoformat()

    resp = supabase.table("pagos").insert(pago).select(SELECT_JOIN).execute()
    # devolver primer registro insertado (con join)
    result = resp.data or []
    return result[0] if result else None

def updatePago(id: int, pago: PagoUpdate):
    datos = {k: v for k, v in pago.dict().items() if v is not None}
    if "date" in datos and isinstance(datos["date"], date):
        datos["date"] = datos["date"].isoformat()
    resp = supabase.table("pagos").update(datos).eq("id", id).select(SELECT_JOIN).execute()
    return resp.data or []

def deletePago(id: int):
    resp = supabase.table("pagos").delete().eq("id", id).execute()
    return resp.data or []