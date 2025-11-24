from pydantic import BaseModel, PositiveFloat, StringConstraints
from typing import Annotated

class Cuarto(BaseModel):
    number: Annotated[str, StringConstraints(min_length=3, max_length=6)]
    type: Annotated[str, StringConstraints(pattern="^(Simple|Doble|Suite|Presidencial)$")]
    status: Annotated[str, StringConstraints(pattern="^(Disponible|Ocupado|Mantenimiento)$")]
    price: PositiveFloat
