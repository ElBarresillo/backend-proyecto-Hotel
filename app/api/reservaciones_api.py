
from fastapi import APIRouter, HTTPException
from app.schemas.reservaciones_schemas import Reservation, ReservationCreate, ReservationUpdate
from app.db.supabase_client import supabase
from app.utils.responses import success_response, error_response

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

# Verificar que el huesped existe
    huesped = supabase.table("huespedes").select("*").eq("id", reservacion.guest_id).execute().data
    if not huesped:
        raise HTTPException(status_code=404, detail=error_response("Huésped no encontrado"))
    
    # Verificar que la Habitacion existe y esta disponible
    habitacion = supabase.table("cuartos").select("*").eq("id", reservacion.room_id).execute().data
    if not habitacion:
        raise HTTPException(status_code=404, detail=error_response("Habitación no encontrada"))

    status = habitacion[0]["status"]
    if status == "Ocupado":
        raise HTTPException(status_code=400, detail=error_response("La habitación ya está ocupada"))
    if status == "Mantenimiento":
        raise HTTPException(status_code=400, detail=error_response("La habitación está en mantenimiento y no se puede reservar"))

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
    
    #Si la reservacion es cancelada o terminada, se libera el cuarto (a menos que este en mantenimiento)
    
    if update.status in ["cancelada", "finalizada"]:
        reservacion = result.data[0]
        habitacion = supabase.table("cuartos").select("*").eq("id", reservacion["room_id"]).execute().data
        if habitacion and habitacion[0]["status"] != "maintenance":
            supabase.table("cuartos").update({"status": "Disponible"}).eq("id", reservacion["room_id"]).execute()

    return success_response(result.data)

# Eliminar reservación
@router.delete("/{id}")
def delete_reservacion(id: int):
    result = supabase.table("reservaciones").delete().eq("id", id).execute()
    if not result.data:
        raise HTTPException(status_code=404, detail="Reservación no encontrada")
    return {"message": "Reservación eliminada"}
