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

