from my_project.auth.dao import bank_account_dao
from my_project.auth.service.general_service import GeneralService


class BankAccountService(GeneralService):
    _dao = bank_account_dao