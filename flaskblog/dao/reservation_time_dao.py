from domain.reservation_time import ReservationTime
from base_dao import BaseDAO

class ReservationTimeDAO(BaseDAO):
    model = ReservationTime

    def _serialize(self, reservation_time):
        return {
            "id": reservation_time.id,
            "check_in_date": reservation_time.check_in_date,
            "check_out_date": reservation_time.check_out_date
        }

    def _update_item(self, reservation_time, data):
        reservation_time.check_in_date = data.get("check_in_date", reservation_time.check_in_date)
        reservation_time.check_out_date = data.get("check_out_date", reservation_time.check_out_date)
