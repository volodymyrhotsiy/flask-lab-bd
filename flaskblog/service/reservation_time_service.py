from base_servise import BaseService
from domain.reservation_time import ReservationTime

class ReservationTimeService(BaseService):
    def create_item(self, data):
        return ReservationTime(check_in_date=data["check_in_date"], check_out_date=data["check_in_date"])