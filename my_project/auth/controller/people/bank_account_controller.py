from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import bank_account_service


class BankAccountController(GeneralController):
    _service = bank_account_service