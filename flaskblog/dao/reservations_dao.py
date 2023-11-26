from domain.reservation import Reservation
from base_dao import BaseDAO

class ReservationDAO(BaseDAO):
    model = Reservation

    def _serialize(self, reservation):
        return {
            "id": reservation.id,
            "total_cost": reservation.totatl_cost,
            "status": reservation.status,
            "person_id": reservation.person_id,
            "reservation_time": reservation.reservation_time
        }

    def _update_item(self, reservation, data):
        reservation.totatl_cost = data.get("total_cost", reservation.totatl_cost)
        reservation.status = data.get("status", reservation.status)
        reservation.person_id = data.get("person_id", reservation.person_id)
        reservation.reservation_time = data.get("reservation_time", reservation.reservation_time)
