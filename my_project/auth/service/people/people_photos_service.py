from my_project.auth.dao import people_photos_dao
from my_project.auth.service.general_service import GeneralService


class PeoplePhotosService(GeneralService):
    _dao = people_photos_dao