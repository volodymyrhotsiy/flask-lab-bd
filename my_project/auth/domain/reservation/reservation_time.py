from __future__ import annotations

from typing import Any

from sqlalchemy import Column, Integer, DateTime
from my_project import db
from sqlalchemy.orm import relationship
from my_project.auth.domain.i_dto import IDto

class ReservationTime(IDto, db.Model):
    __tablename__ = "reservation_time"
    id = Column(Integer, primary_key=True)
    check_in_date = Column(DateTime, nullable=False)
    check_out_date = Column(DateTime, nullable=False)
    reservation = relationship("Reservation", backref="reservation_time", lazy=True)

    def __repr__(self):
        return f"ReservationTime(check_in_date={self.check_in_date}, check_out_date={self.check_out_date})"

    @staticmethod
    def create_from_dto(dto_dict: dict[str, Any]) -> ReservationTime:
        obj = ReservationTime(
            id = dto_dict.get("id"),
            check_in_date = dto_dict.get("check_in_date"),
            check_out_date = dto_dict.get("check_out_date"),
        )
        return obj
    
    def put_into_dto(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "check_in_date": self.check_in_date,
            "check_out_date": self.check_out_date,
        }