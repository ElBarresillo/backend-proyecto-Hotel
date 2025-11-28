from pydantic import BaseModel, Field
from typing import Optional

class CargosBase(BaseModel):
    reservation_id: int = Field(..., description="ID de la reservacion asociada al cargo", example=7)
    description: str = Field(..., description="Descripcion del cargo extra", example="Servicio de lavanderia")
    amount: float = Field(..., description="Monto del cargo extra", example=250)

class CargosCreate(CargosBase):
    pass

class CargosUpdate(BaseModel):
    description: Optional[str] = Field(None, description="Nueva descripcion del cargo", example="Servicio de spa")
    amount: Optional[float] = Field(None, description="Nuevo monto del cargo", example=300)


# Modelos de respuesta / lectura compatibles con los routers
class Cargo(CargosBase):
    id: int = Field(..., description="ID unico del cargo", example=1)

    class Config:
        from_attributes = True


# Aliases para mantener compatibilidad con nombres usados en el API
class CargoCreate(CargosBase):
    pass

class CargoUpdate(CargosUpdate):
    pass

