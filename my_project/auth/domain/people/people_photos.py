from __future__ import annotations

from typing import Any

from sqlalchemy import Column, String, Integer, ForeignKey
from my_project import db
from my_project.auth.domain.i_dto import IDto

class PeoplePhotos(IDto, db.Model):
    __tablename__ = "peoplephotos"
    
    id = Column(Integer, primary_key=True)
    photo_url = Column(String(45))
    people_id = Column(Integer, ForeignKey("people.id"), nullable=False)

    def __repr__(self):
        return f"(Photo of {self.persone.id} '{self.photo_url}')"
    
    @staticmethod
    def create_from_dto(dto_dict: dict[str, Any]) -> PeoplePhotos:
        obj = PeoplePhotos(
            id = dto_dict.get("id"),
            photo_url = dto_dict.get("photo_url"),
            people_id = dto_dict.get("people_id"),
        )
        return obj
    
    def put_into_dto(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "photo_url": self.photo_url,
            "people_id": self.person_id,
        }