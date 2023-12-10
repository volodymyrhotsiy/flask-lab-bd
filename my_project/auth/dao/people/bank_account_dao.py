from my_project.auth.dao.gereral_dao import GeneralDAO
from my_project.auth.domain.people.bank_account import BankAccount


class BankAccountDao(GeneralDAO):
    _domain_type = BankAccount