from domain.bank_account import BankAccount
from base_dao import BaseDAO

class BankAccountDAO(BaseDAO):
    model = BankAccount

    def _serialize(self, bank_account):
        return {"id": bank_account.id, "account_name": bank_account.account_name, "person_id": bank_account.person_id}

    def _update_item(self, bank_account, data):
        bank_account.account_name = data.get("account_name", bank_account.account_name)

