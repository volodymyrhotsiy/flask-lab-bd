from my_project.auth.dao.gereral_dao import GeneralDAO
from my_project.auth.domain.property.property import Property


class PropertyDao(GeneralDAO):
    _domain_type = Property