from pydantic import BaseModel
from typing import Optional

class CargosBase(BaseModel):
    reservation_id: int
    description: str
    amount: float

class CargosCreate(CargosBase):
    pass

class CargosUpdate(BaseModel):
    description: Optional[str] = None
    amount: Optional[float] = None


# Modelos de respuesta / lectura compatibles con los routers
class Cargo(CargosBase):
    id: int

    class Config:
        orm_mode = True


# Aliases para mantener compatibilidad con nombres usados en el API
class CargoCreate(CargosBase):
    pass

class CargoUpdate(CargosUpdate):
    pass

