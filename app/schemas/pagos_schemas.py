# app/schemas/pagos_schemas.py
from pydantic import BaseModel
from typing import Optional
from datetime import date

class Guest(BaseModel):
    name: str

    class Config:
        from_attributes = True

class Reservation(BaseModel):
    id: int
    room_id: int
    guest_id: int
    checkin_date: date
    checkout_date: date
    huespedes: Guest

    class Config:
        from_attributes = True

class PagoBase(BaseModel):
    reservation_id: int
    amount: float
    date: date
    method: str
    status: Optional[str] = "Pendiente"

class PagoCreate(PagoBase):
    pass

class PagoUpdate(BaseModel):
    reservation_id: Optional[int] = None
    amount: Optional[float] = None
    date: Optional[date] = None
    method: Optional[str] = None
    status: Optional[str] = None

class Pago(PagoBase):
    id: int
    reservaciones: Optional[Reservation]

    class Config:
        from_attributes = True