from pydantic import BaseModel


class Address(BaseModel):
    email: str
    address: str
    lat: float
    long: float

    class Config:
        orm_mode = True