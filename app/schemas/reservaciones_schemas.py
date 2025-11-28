from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

class ReservationBase(BaseModel):
    room_id: int = Field(..., description="ID del cuarto reservado", example=5)
    guest_id: int = Field(..., description="ID del huesped que realiza la reservacion", example=2)
    checkin_date: date = Field(..., description="Fecha de entrada (YYYY-MM-DD)", example="2023-12-01")
    checkout_date: date = Field(..., description="Fecha de salida (YYYY-MM-DD)", example="2023-12-05")
    status: Optional[str] = Field("pendiente", description="Estado de la reservacion", example="pendiente")

class ReservationCreate(ReservationBase):
    pass

class ReservationUpdate(BaseModel):
    status: str = Field(..., description="Nuevo estado de la reservacion", example="confirmada")

class Reservation(ReservationBase):
    id: int = Field(..., description="ID unico de la reservacion", example=1)

    class Config:
        from_attributes = True
