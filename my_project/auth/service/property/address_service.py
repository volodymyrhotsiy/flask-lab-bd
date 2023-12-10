from my_project.auth.dao import address_dao
from my_project.auth.service.general_service import GeneralService


class AddressService(GeneralService):
    _dao = address_dao