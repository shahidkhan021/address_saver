from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,Float
from sqlalchemy.orm import relationship
from dataclasses import dataclass

from database import Base

class Address(Base):
    __tablename__ = "address"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    address = Column(String)
    lat = Column(Float)
    long = Column(Float)

    # items = relationship("Item", back_populates="owner")


# class Item(Base):
#     __tablename__ = "items"

#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, index=True)
#     description = Column(String, index=True)
#     owner_id = Column(Integer, ForeignKey("users.id"))

#     owner = relationship("User", back_populates="items")