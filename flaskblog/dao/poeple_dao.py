from domain.people import Persone
from base_dao import BaseDAO

class PeopleDAO(BaseDAO):
    model = Persone

    def _serialize(self, persone):
        return {"id": persone.id, "person_first_name": persone.first_name, "person_last_name": persone.last_name}

    def _update_item(self, bank_account, data):
        bank_account.account_name = data.get("account_name", bank_account.account_name)

