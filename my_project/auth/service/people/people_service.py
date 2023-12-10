from my_project.auth.dao import people_dao
from my_project.auth.service.general_service import GeneralService


class PeopleService(GeneralService):
    _dao = people_dao