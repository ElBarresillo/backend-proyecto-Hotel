from fastapi import APIRouter, HTTPException
from app.schemas.reservaciones_schemas import Reservation, ReservationCreate, ReservationUpdate
from app.db.supabase_client import supabase

router = APIRouter(prefix="/reservaciones", tags=["Reservaciones"])

# Listar todas las reservaciones
@router.get("/", response_model=list[Reservation])
def get_reservaciones():
    result = supabase.table("reservaciones").select("*").execute()
    return result.data

# Obtener una reservación por ID
@router.get("/{id}", response_model=Reservation)
def get_reservacion(id: int):
    result = supabase.table("reservaciones").select("*").eq("id", id).execute()
    if not result.data:
        raise HTTPException(status_code=404, detail="Reservación no encontrada")
    return result.data[0]

# Crear una reservación (validando disponibilidad)
@router.post("/", response_model=Reservation)
def create_reservacion(reservacion: ReservationCreate):
    # Validar disponibilidad
    existing = supabase.table("reservaciones").select("*").eq("room_id", reservacion.room_id).execute()
    for r in existing.data:
        if not (reservacion.checkout_date <= r["checkin_date"] or reservacion.checkin_date >= r["checkout_date"]):
            raise HTTPException(status_code=400, detail="Habitación no disponible en esas fechas")

    # Insertar
    data = {
        "room_id": reservacion.room_id,
        "guest_id": reservacion.guest_id,
        "checkin_date": str(reservacion.checkin_date),
        "checkout_date": str(reservacion.checkout_date),
        "status": reservacion.status
    }
    result = supabase.table("reservaciones").insert(data).execute()
    return result.data[0]

# Actualizar estado (check-in / check-out)
@router.put("/{id}", response_model=Reservation)
def update_reservacion(id: int, update: ReservationUpdate):
    result = supabase.table("reservaciones").update({"status": update.status}).eq("id", id).execute()
    if not result.data:
        raise HTTPException(status_code=404, detail="Reservación no encontrada")

# Eliminar reservación
@router.delete("/{id}")
def delete_reservacion(id: int):
    result = supabase.table("reservaciones").delete().eq("id", id).execute()
    if not result.data:
        raise HTTPException(status_code=404, detail="Reservación no encontrada")
    return {"message": "Reservación eliminada"}
