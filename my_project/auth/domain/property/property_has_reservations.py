from __future__ import annotations

from typing import Any

from sqlalchemy import Column, Integer, ForeignKey
from my_project import db
from my_project.auth.domain.i_dto import IDto

class PropertyHasReservations(IDto, db.Model):
    id = Column(Integer, primary_key=True)
    property_id = Column(Integer, ForeignKey("property.id"), nullable=False)
    reservation_id = Column(Integer, ForeignKey("reservation.id"), nullable=False)

    def __repr__(self):
        return f"PropertyHasReservations(property_id={self.property_id}, reservation_id={self.reservation_id})"
    
    @staticmethod
    def create_from_dto(dto_dict: dict[str, Any]) -> PropertyHasReservations:
        obj = PropertyHasReservations(
            id = dto_dict.get("id"),
            property_id = dto_dict.get("property_id"),
            reservation_id = dto_dict.get("reservation_id"),
        )
        return obj
    
    def put_into_dto(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "property_id": self.property_id,
            "reservation_id": self.reservation_id,
        }