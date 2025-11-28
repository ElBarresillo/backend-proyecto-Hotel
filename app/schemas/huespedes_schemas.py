from pydantic import BaseModel, EmailStr, StringConstraints, Field
from typing import Annotated

class Huesped(BaseModel):
    name: Annotated[str, StringConstraints(min_length=3, max_length=45)] = Field(..., description="Nombre completo del huesped", example="Juan Perez")
    phone: Annotated[str, StringConstraints(min_length=10, max_length=12, pattern=r'^\+?\d+$')] = Field(..., description="Numero de telefono del huesped (puede incluir '+')", example="521234567890")
    email: EmailStr = Field(..., description="Correo electronico del huesped", example="juan.perez@correo.com")
