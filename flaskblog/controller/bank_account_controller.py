from base_controller import BaseController
from service.bank_account_service import BankAccountService

class BankAccountController(BaseController):
    def __init__(self):
        super().__init__(BankAccountService())