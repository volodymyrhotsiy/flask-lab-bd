from base_controller import BaseController
from service.reservation_service import ReservationService

class ReservationController(BaseController):
    def __init__(self):
        super().__init__(ReservationService())