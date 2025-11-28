from pydantic import BaseModel, Field
from typing import Optional

class LoginBase(BaseModel):
    email: str = Field(..., description="Correo electronico")
    password: str = Field(..., description="Contraseña del usuario", example="123456")

class UsuarioCreate(LoginBase):
    pass