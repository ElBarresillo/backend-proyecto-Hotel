
from pydantic import BaseModel
from datetime import date
from typing import Optional

class ReservationBase(BaseModel):
    room_id: int
    guest_id: int
    checkin_date: date
    checkout_date: date
    status: Optional[str] = "pendiente"

class ReservationCreate(ReservationBase):
    pass

class ReservationUpdate(BaseModel):
    status: str

class Reservation(ReservationBase):
    id: int

    class Config:
        orm_mode = True
