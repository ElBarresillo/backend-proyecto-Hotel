from fastapi import APIRouter, HTTPException
from app.schemas.reservaciones_schemas import Reservation, ReservationCreate, ReservationUpdate
import app.crud.crud_reservaciones as crud
import app.services.reservaciones_services as service

router = APIRouter(prefix="/reservaciones", tags=["Reservaciones"])

# Listar todas las reservaciones
@router.get("/", response_model=list[Reservation])
def get_reservaciones():
    result = crud.obtenerReservaciones()
    return result

# Obtener una reservación por ID
@router.get("/{id}", response_model=Reservation)
def get_reservacion(id: int):
    result = crud.obtenerReservacionesID(id)
    if not result:
        raise HTTPException(status_code=404, detail="Reservación no encontrada")
    return result

# Crear una reservación (validando disponibilidad)
@router.post("/", response_model=Reservation)
def create_reservacion(reservacion: ReservationCreate):
    return service.process_new_reservation(reservacion)

# Actualizar estado (check-in / check-out)
@router.put("/{id}", response_model=Reservation)
def update_reservacion(id: int, update: ReservationUpdate):
    return service.process_update_status(id, update)

# Eliminar reservación
@router.delete("/{id}")
def delete_reservacion(id: int):
    result = crud.deleteReservacion(id)
    if not result:
        raise HTTPException(status_code=404, detail="Reservación no encontrada")
    return {"message": "Reservación eliminada"}