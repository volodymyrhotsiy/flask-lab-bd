from __future__ import annotations

from typing import Any

from sqlalchemy import Column, Integer
from my_project import db
from sqlalchemy.orm import relationship
from my_project.auth.domain.i_dto import IDto

class PropertyStats(IDto, db.Model):
    __tablename__ = "property_stats"
    id = Column(Integer, primary_key=True)
    number_of_bedrooms = Column(Integer, nullable=False)
    number_of_bathrooms = Column(Integer, nullable=False)
    max_guests = Column(Integer, nullable=False)
    price_per_night = Column(Integer, nullable=False)
    property = relationship("Property", backref="property_stats", lazy=True)

    def __repr__(self):
        return f"PropertyStats(number_of_bedrooms={self.number_of_bedrooms}, number_of_bathrooms={self.number_of_bathrooms}, max_guests={self.max_guests}, price_per_night={self.price_per_night})"

    
    @staticmethod
    def create_from_dto(dto_dict: dict[str, Any]) -> PropertyStats:
        obj = PropertyStats(
            id = dto_dict.get("id"),
            number_of_bedrooms = dto_dict.get("number_of_bedrooms"),
            number_of_bathrooms = dto_dict.get("number_of_bathrooms"),
            max_guests = dto_dict.get("max_guests"),
            price_per_night = dto_dict.get("price_per_night"),
        )
        return obj
    
    def put_into_dto(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "number_of_bedrooms": self.number_of_bedrooms,
            "number_of_bathrooms": self.number_of_bathrooms,
            "max_guests": self.max_guests,
            "price_per_night": self.price_per_night,
        }