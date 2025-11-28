from pydantic import BaseModel, Field
from typing import Optional

class PagoBase(BaseModel):
    reservation_id: int = Field(..., description="ID de la reservacion asociada al pago", example=10)
    amount: float = Field(..., description="Monto pagado", example=1500)
    date: str = Field(..., description="Fecha del pago en formato YYYY-MM-DD", example="2023-11-27")
    method: str = Field(..., description="Metodo de pago utilizado", example="Tarjeta de credito")

class PagoCreate(PagoBase):
    pass

class PagoUpdate(BaseModel):
    amount: Optional[float] = Field(None, description="Nuevo monto pagado", example=1600)
    date: Optional[str] = Field(None, description="Nueva fecha del pago en formato YYYY-MM-DD", example="2023-11-28")
    method: Optional[str] = Field(None, description="Nuevo metodo de pago", example="Efectivo")


# Modelo de respuesta / lectura
class Pago(PagoBase):
    id: int = Field(..., description="ID unico del pago", example=1)

    class Config:
        from_attributes = True




