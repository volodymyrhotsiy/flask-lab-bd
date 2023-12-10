from my_project.auth.dao.gereral_dao import GeneralDAO
from my_project.auth.domain.reservation.reservation_history import ReservationHistory


class ReservationHistoryDao(GeneralDAO):
    _domain_type = ReservationHistory