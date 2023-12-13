from __future__ import annotations

from typing import Any

from sqlalchemy import Column, Integer, ForeignKey
from my_project import db
from sqlalchemy.orm import relationship
from my_project.auth.domain.i_dto import IDto

class ReservationHistory(IDto, db.Model):
    __tablename__ = "reservation_history"
    id = Column(Integer, primary_key=True)
    reservation_id = Column(Integer, ForeignKey("reservation.id"), nullable=False)
    people_id = Column(Integer, ForeignKey("people.id"), nullable=False)

    def __repr__(self):
        return f"ReservationHistory(peeople_id={self.people_id})"

    @staticmethod
    def create_from_dto(dto_dict: dict[str, Any]) -> ReservationHistory:
        obj = ReservationHistory(
            id = dto_dict.get("id"),
            reservation_id = dto_dict.get("reservation_id"),
            peeople_id = dto_dict.get("people_id"),
        )
        return obj
    
    def put_into_dto(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "reservation_id": self.reservation_id,
            "people_id": self.people_id,
        }