from fastapi import  APIRouter, HTTPException
from app.db.supabase_client import supabase
from app.schemas.pagos_schemas import Pago, PagoCreate
from app.utils.responses import success_response, error_response

router = APIRouter(prefix="/pagos", tags=["Pagos"])

#Obtener todos los pagos 
@router.get("/" , response_model=list[Pago],
            summary="Listar pagos",
            description="Obtiene la lista de todos los pagos registrados en el sistema.",
            response_description="Lista de pagos.")
def listar_pagos():
    resultado = supabase.table("pagos").select("*").execute() 
    return resultado.data

#Obtener un pago por ID
@router.get("/{id}", response_model=Pago)
def obtener_pago(id: int):
    resultado = supabase.table("pagos").select("*").eq("id", id).execute()
    if resultado.data:
        return resultado.data[0]
    raise HTTPException(status_code=404, detail=error_response("Error: Pago no encontrado"))


#Crear un nuevo pago
@router.post("/", response_model=Pago)
def crear_pago(pago: PagoCreate):
    # Realizar verificacion de la reservacion
    reservacion = supabase.table("reservaciones").select("*").eq("id", pago.reservation_id).execute().data
    if not reservacion:
        raise HTTPException(status_code=404, detail=error_response("Error: Reservación no encontrada"))
    # Insertar el pago 
    data = {
        "reservation_id": pago.reservation_id,
        "amount": pago.amount,
        "date": pago.date,
        "method": pago.method
    }
    resultado = supabase.table("pagos").insert(data).execute()
    return resultado.data[0]

#Actualizar un pago por ID
@router.put("/{id}", response_model=Pago)
def actualizar_pago(id: int, pago: PagoCreate):
    resultado = supabase.table("pagos").select("*").eq("id", id).execute()
    if not resultado.data:
        raise HTTPException(status_code=404, detail=error_response("Error: Pago no encontrado"))
    data = {
        "reservation_id": pago.reservation_id,
        "amount": pago.amount,
        "date": pago.date,
        "method": pago.method
    }
    actualizado = supabase.table("pagos").update(data).eq("id", id).execute()
    return actualizado.data[0]

#Eliminar un pago por ID
@router.delete("/{id}")
def eliminar_pago(id: int):
    resultado = supabase.table("pagos").select("*").eq("id", id).execute()
    if not resultado.data:
        raise HTTPException(status_code=404, detail=error_response("Error: Pago no encontrado"))
    supabase.table("pagos").delete().eq("id", id).execute()
    return success_response("Pago eliminado correctamente")