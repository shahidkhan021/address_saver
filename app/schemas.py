from pydantic import BaseModel


class Address(BaseModel):
    email: str
    address: str
    lat: float
    long: float

    class Config:
        orm_mode = True

class Latitude(BaseModel):
    lat: float

class Longitude(BaseModel):
    long: float

class Email(BaseModel):
    email: str

class AddressList(BaseModel):
    address_list: list[Address] = []