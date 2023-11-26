from domain.reservation_history import ReservationHistory
from base_dao import BaseDAO

class ReservationHistoryDAO(BaseDAO):
    model = ReservationHistory

    def _serialize(self, reservation_history):
        return {
            "id": reservation_history.id,
            "person_id": reservation_history.person_id
        }

    def _update_item(self, reservation_history, data):
        reservation_history.person_id = data.get("person_id", reservation_history.person_id)
