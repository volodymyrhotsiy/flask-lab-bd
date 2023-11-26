from base_servise import BaseService
from domain.service import Service

class ServiceService(BaseService):
    def create_item(self, data):
        return Service(bank_account_first=data["bank_account_first "],bank_account_second=data["bank_account_second"], reservation_id=data["reservation_id"])