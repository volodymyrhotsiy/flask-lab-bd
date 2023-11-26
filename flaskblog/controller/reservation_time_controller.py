from service.reservation_time_service import ReservationTimeService
from base_controller import BaseController

class ReservationTimeController(BaseController):
    def __init__(self):
        super().__init__(ReservationTimeService())
