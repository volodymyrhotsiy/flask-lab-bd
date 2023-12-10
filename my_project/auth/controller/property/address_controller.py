from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import address_service


class AddressController(GeneralController):
    _service = address_service