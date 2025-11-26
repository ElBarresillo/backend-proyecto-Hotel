from fastapi import HTTPException
from app.crud import crud_reservaciones, crud_cuartos, crud_huespedes
from app.schemas.reservaciones_schemas import ReservationCreate, ReservationUpdate

def process_new_reservation(reservacion: ReservationCreate):
    # Verificar que el huesped existe
    if not crud_huespedes.obtenerHuespedId(reservacion.guest_id):
        raise HTTPException(status_code=404, detail="Huésped no encontrado")
    
    # Verificar habitación
    habitacion = crud_cuartos.obtenerCuartoId(reservacion.room_id)
    if not habitacion:
        raise HTTPException(status_code=404, detail="Habitación no encontrada")

    status = habitacion["status"]
    if status == "Ocupado":
        raise HTTPException(status_code=400, detail="La habitación ya está ocupada")
    if status == "Mantenimiento":
        raise HTTPException(status_code=400, detail="La habitación está en mantenimiento")

    # Validar disponibilidad de fechas
    existing_reservations = crud_reservaciones.obtenerReservacionPorCuarto(reservacion.room_id)
    
    checkin = reservacion.checkin_date
    checkout = reservacion.checkout_date
    
    for r in existing_reservations:
        # Convertimos fechas de string a objeto si es necesario
        r_checkin = r["checkin_date"]
        r_checkout = r["checkout_date"]
        if not (str(checkout) <= str(r_checkin) or str(checkin) >= str(r_checkout)):
            raise HTTPException(status_code=400, detail="Habitación no disponible en esas fechas")

    data = {
        "room_id": reservacion.room_id,
        "guest_id": reservacion.guest_id,
        "checkin_date": str(reservacion.checkin_date),
        "checkout_date": str(reservacion.checkout_date),
        "status": reservacion.status
    }
    
    nueva_reservacion = crud_reservaciones.crearReservacion(data)

    crud_cuartos.updateCuartoEstado(reservacion.room_id, "Ocupado")
            
    return nueva_reservacion

def process_update_status(id: int, update: ReservationUpdate):
    # Validar existencia
    if not crud_reservaciones.obtenerReservacionesID(id):
        raise HTTPException(status_code=404, detail="Reservación no encontrada")
        
    result = crud_reservaciones.updateEstadoReservacion(id, update.status)
    
    # Lógica de liberar cuarto si se cancela/finaliza
    if update.status in ["cancelada", "finalizada"]:
        reservacion = result[0]
        habitacion = crud_cuartos.obtenerCuartoId(reservacion["room_id"])
        
        if habitacion and habitacion["status"] != "Mantenimiento":
            crud_cuartos.updateCuartoEstado(reservacion["room_id"], "Disponible")
            
    return result