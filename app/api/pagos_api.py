# app/api/pagos_api.py
from fastapi import APIRouter, HTTPException
import app.crud.crud_pagos as crud
from app.schemas.pagos_schemas import PagoCreate, PagoUpdate
from app.utils.responses import success_response, error_response

router = APIRouter(prefix="/pagos", tags=["Pagos"])

@router.get("/")
def listar_pagos():
    data = crud.obtenerTodosPagos()
    return success_response(data)

@router.get("/{id}")
def obtener_pago(id: int):
    data = crud.obtenerPagoId(id)
    if not data:
        raise HTTPException(status_code=404, detail="Pago no encontrado")
    return success_response(data)

@router.post("/")
def crear_pago(pago: PagoCreate):
    data = crud.crearPago(pago.dict())
    if not data:
        raise HTTPException(status_code=400, detail="No se pudo crear el pago")
    return success_response(data)

@router.put("/{id}")
def actualizar_pago(id: int, pago: PagoUpdate):
    existente = crud.obtenerPagoId(id)
    if not existente:
        raise HTTPException(status_code=404, detail="Pago no encontrado")
    data = crud.updatePago(id, pago)
    return success_response(data)

@router.delete("/{id}")
def eliminar_pago(id: int):
    existente = crud.obtenerPagoId(id)
    if not existente:
        raise HTTPException(status_code=404, detail="Pago no encontrado")
    crud.deletePago(id)
    return success_response("Pago eliminado correctamente")