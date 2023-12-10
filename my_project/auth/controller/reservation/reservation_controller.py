from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import reservation_service


class ReservationController(GeneralController):
    _service = reservation_service