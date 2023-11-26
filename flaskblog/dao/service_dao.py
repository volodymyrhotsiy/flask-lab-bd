from domain.service import Service
from base_dao import BaseDAO

class ServiceDAO(BaseDAO):
    model = Service

    def _serialize(self, service):
        return {
            "id": service.id,
            "bank_account_first": service.bank_account_first,
            "bank_account_second": service.bank_account_second,
            "reservation_id": service.reservation_id
        }

    def _update_item(self, service, data):
        service.bank_account_first = data.get("bank_account_first", service.bank_account_first)
        service.bank_account_second = data.get("bank_account_second", service.bank_account_second)
        service.reservation_id = data.get("reservation_id", service.reservation_id)
