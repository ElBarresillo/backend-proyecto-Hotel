from pydantic import BaseModel
from typing import Optional

class PagoBase(BaseModel):
    reservation_id: int
    amount: float
    date: str 
    method: str

class PagoCreate(PagoBase):
    pass

class PagoUpdate(BaseModel):
    amount: Optional[float] = None
    date: Optional[str] = None
    method: Optional[str] = None


# Modelo de respuesta / lectura
class Pago(PagoBase):
    id: int

    class Config:
        orm_mode = True




