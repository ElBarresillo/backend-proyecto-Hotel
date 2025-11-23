from pydantic import BaseModel

class Huesped(BaseModel):
    name: str
    phone: str
    email: str
