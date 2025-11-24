from pydantic import BaseModel, EmailStr, StringConstraints
from typing import Annotated

class Huesped(BaseModel):
    name: Annotated[str, StringConstraints(min_length=3, max_length=45)]
    phone: Annotated[str, StringConstraints(min_length=10, max_length=12, pattern=r'^\+?\d+$')]
    email: EmailStr
