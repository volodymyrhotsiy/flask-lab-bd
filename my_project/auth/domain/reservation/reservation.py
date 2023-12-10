from __future__ import annotations

from typing import Any

from sqlalchemy import Column, Integer, ForeignKey, Float, String
from my_project import db
from sqlalchemy.orm import relationship
from my_project.auth.domain.i_dto import IDto

class Reservation(IDto, db.Model):
    id = Column(Integer, primary_key=True)
    total_cost = Column(Float, nullable=False)
    status = Column(String(20), nullable=False)
    people_id = Column(Integer, ForeignKey("people.id"), nullable=False)
    reservation_time_id = Column(Integer, ForeignKey("reservation_time.id"), nullable=False)

    properties = relationship("PropertyHasReservations", backref="reservations", lazy=True)
    reservation_history = relationship("ReservationHistory", backref="reservation_history", lazy=True)

    def __repr__(self):
        return f"Reservation(total_cost={self.total_cost}, status='{self.status}', people_id={self.people_id}, reservation_time={self.reservation_time})"
    
    @staticmethod
    def create_from_dto(dto_dict: dict[str, Any]) -> Reservation:
        obj = Reservation(
            id = dto_dict.get("id"),
            total_cost = dto_dict.get("total_cost"),
            status = dto_dict.get("status"),
            people_id = dto_dict.get("people_id"),
            reservation_time_id = dto_dict.get("reservation_time_id"),
        )
        return obj
    
    def put_into_dto(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "total_cost": self.total_cost,
            "status": self.status,
            "people_id": self.people_id,
            " reservation_time_id": self. reservation_time_id,
        }