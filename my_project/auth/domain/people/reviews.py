from __future__ import annotations

from typing import Any

from sqlalchemy import Column, ForeignKey
from datetime import datetime
from my_project import db
from my_project.auth.domain.i_dto import IDto

class Reviews(IDto, db.Model):
    __tablename__ = "reviews"

    id =Column(db.Integer, primary_key=True)
    rating =Column(db.Float(), nullable=False)
    comment =Column(db.String(45))
    review_date =Column(db.DateTime, nullable=False, default=datetime.utcnow)
    people_id =Column(db.Integer,ForeignKey("people.id"), nullable=False)

    def __repr__(self):
        return f"Review(rating={self.rating}, comment='{self.comment}', review_date={self.review_date})"
    
    @staticmethod
    def create_from_dto(dto_dict: dict[str, Any]) -> Reviews:
        obj = Reviews(
            id = dto_dict.get("id"),
            rating = dto_dict.get("rating"),
            comment = dto_dict.get("comment"),
            review_date = dto_dict.get("review_date"),
            people_id = dto_dict.get("people_id"),
        )
        return obj
    
    def put_into_dto(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "rating": self.rating,
            "comment": self.comment,
            "review_date": self.review_date,
            "people_id": self.people_id,
        }