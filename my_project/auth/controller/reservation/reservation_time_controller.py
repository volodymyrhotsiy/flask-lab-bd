from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import reservation_time_service


class ReservationTimeController(GeneralController):
    _service = reservation_time_service