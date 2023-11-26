from base_servise import BaseService
from domain.bank_account import BankAccount

class BankAccountService(BaseService):
    def create_item(self, data):
        return BankAccount(account_name=data["account_name"], person_id=data["person_id"])