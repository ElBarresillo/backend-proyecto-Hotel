from pydantic import BaseModel
class Cuarto(BaseModel):
    number: str
    type: str
    status: str
    price: float
