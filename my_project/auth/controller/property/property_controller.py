from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import property_service


class PropertyController(GeneralController):
    _service = property_service