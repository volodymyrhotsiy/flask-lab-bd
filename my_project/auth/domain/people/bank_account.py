from __future__ import annotations

from typing import Any

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from my_project import db
from my_project.auth.domain.i_dto import IDto

class BankAccount(IDto, db.Model):
    __talbename__ = "bankaccount"
    id = Column(Integer, primary_key=True)
    account_name = Column(String(45), nullable=False)
    people_id = Column(Integer, ForeignKey("people.id"), nullable=False)

    def __repr__(self):
        return f"BankAccount('{self.account_name}')"
    
    @staticmethod
    def create_from_dto(dto_dict: dict[str, Any]) -> BankAccount:
        obj = BankAccount(
            id = dto_dict.get("id"),
            account_name = dto_dict.get("account_name"),
            people_id = dto_dict.get("people_id"),
            service = dto_dict.get("service"),
        )
        return obj
    
    def put_into_dto(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "account_name": self.account_name,
            "people_id": self.people_id,
            "service": self.service,
        }