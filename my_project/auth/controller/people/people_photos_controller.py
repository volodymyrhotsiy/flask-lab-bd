from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import people_photos_service


class PeoplePhotosController(GeneralController):
    _service = people_photos_service