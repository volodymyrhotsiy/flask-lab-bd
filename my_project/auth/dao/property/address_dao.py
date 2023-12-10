from my_project.auth.dao.gereral_dao import GeneralDAO
from my_project.auth.domain.property.address import Address


class AddressDao(GeneralDAO):
    _domain_type = Address