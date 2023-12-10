from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import people_service


class PeopleController(GeneralController):
    _service = people_service