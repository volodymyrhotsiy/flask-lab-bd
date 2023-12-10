from __future__ import annotations

from typing import Any

from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from my_project import db
from my_project.auth.domain.i_dto import IDto

class People(IDto, db.Model):
    __tablename__ = "people"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    photos = relationship("PeoplePhotos", backref="people", lazy=True)
    reviews = relationship("Reviews", backref="people", lazy=True)
    account = relationship("BankAccount", backref="people", lazy=True)
    property = relationship("Property", backref="people", lazy=True)
    reservation = relationship("Reservation", backref="people", lazy=True)
    reservation_hitsory = relationship(
        "ReservationHistory", backref="people", lazy=True
    )

    def __repr__(self):
        return f"People('{self.first_name}' {self.last_name})"  
    
    @staticmethod
    def create_from_dto(dto_dict: dict[str, Any]) -> People:
        obj = People(
            id = dto_dict.get("id"),
            first_name = dto_dict.get("first_name"),
            last_name = dto_dict.get("last_name"),
        )
        return obj
    
    def put_into_dto(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
        }