from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import reservation_history_service


class ReservationHistoryController(GeneralController):
    _service = reservation_history_service