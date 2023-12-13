from __future__ import annotations

from typing import Any

from sqlalchemy import Column, String, Integer
from my_project import db
from sqlalchemy.orm import relationship
from my_project.auth.domain.i_dto import IDto

class Address(IDto, db.Model):
    __tablename__ = "address"

    id = Column(Integer, primary_key=True)
    state = Column(String(30), nullable=False)
    street = Column(String(30), nullable=False)
    street_number = Column(String(30), nullable=False)
    property = relationship("Property", backref="property_address", lazy=True)
    city_id = Column(Integer)

    def __repr__(self):
        return f"Adress(state='{self.state}', street='{self.street}', street_number='{self.street_number}')"

    
    @staticmethod
    def create_from_dto(dto_dict: dict[str, Any]) -> Address:
        obj = Address(
            id = dto_dict.get("id"),
            state = dto_dict.get("state"),
            street = dto_dict.get("street"),
            street_number = dto_dict.get("street_number"),
            city_id = dto_dict.get("city_id "),
        )
        return obj
    
    def put_into_dto(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "state": self.state,
            "street": self.street,
            "street_number": self.street_number,
            "city_id ": self.city_id, 
        }