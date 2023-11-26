from base_servise import BaseService
from domain.reservation_history import ReservationHistory

class ReservationHistoryService(BaseService):
    def create_item(self, data):
        return ReservationHistory(reservations_id=data["reservations_id"], people_id=data["people_id"])