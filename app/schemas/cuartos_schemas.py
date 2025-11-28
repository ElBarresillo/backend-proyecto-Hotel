from pydantic import BaseModel, PositiveFloat, StringConstraints, Field
from typing import Annotated

class Cuarto(BaseModel):
    number: Annotated[str, StringConstraints(min_length=3, max_length=6)] = Field(..., description="Numero identificador del cuarto", example="101")
    type: Annotated[str, StringConstraints(pattern="^(Simple|Doble|Suite|Presidencial)$")] = Field(..., description="Tipo de cuarto", example="Suite")
    status: Annotated[str, StringConstraints(pattern="^(Disponible|Ocupado|Mantenimiento)$")] = Field(..., description="Estado actual del cuarto", example="Disponible")
    price: PositiveFloat = Field(..., description="Precio por noche del cuarto", example=1500)
