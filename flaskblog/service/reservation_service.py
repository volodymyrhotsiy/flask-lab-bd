from base_servise import BaseService
from domain.reservation import Reservation

class ReservationService(BaseService):
    def create_item(self, data):
        return Reservation(total_cost=data["total_cost"], status=data["status"], people_id=data["people_id"], reservation_time_id=data["reservation_time_id"])