from pydantic import BaseModel
from typing import Optional

class LoginBase(BaseModel):
    email: str
    password: str

class UsuarioCreate(LoginBase):
    pass