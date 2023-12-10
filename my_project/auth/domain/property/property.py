from __future__ import annotations

from typing import Any

from sqlalchemy import Column, ForeignKey
from my_project import db
from sqlalchemy.orm import relationship
from my_project.auth.domain.i_dto import IDto

class Property(IDto, db.Model):
    id = Column(db.Integer, primary_key=True)
    people_id = Column(db.Integer, ForeignKey("people.id"), nullable=False)
    property_stats_id = Column(db.Integer, ForeignKey("property_stats.id"), nullable=False)
    address_id = Column(db.Integer, ForeignKey("address.id"), nullable=False)

    def __repr__(self):
        return f"Property(people_id={self.people_id}, property_stats={self.property_stats}, property_adress={self.property_adress})"

    
    @staticmethod
    def create_from_dto(dto_dict: dict[str, Any]) -> Property:
        obj = Property(
            id = dto_dict.get("id"),
            people_id = dto_dict.get("people_id"),
            property_stats_id = dto_dict.get("property_stats_id"),
            address_id = dto_dict.get("address_id"),
        )
        return obj
    
    def put_into_dto(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "people_id": self.people_id,
            "property_stats_id": self.property_stats_id,
            "address_id": self.address_id,
        }