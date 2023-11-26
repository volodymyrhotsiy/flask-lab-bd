from service.reservation_history_service import ReservationHistoryService
from base_controller import BaseController

class ReservationHistoryController(BaseController):
    def __init__(self):
        super().__init__(ReservationHistoryService())
