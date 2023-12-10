from my_project.auth.dao import property_dao
from my_project.auth.service.general_service import GeneralService


class PropertyService(GeneralService):
    _dao = property_dao