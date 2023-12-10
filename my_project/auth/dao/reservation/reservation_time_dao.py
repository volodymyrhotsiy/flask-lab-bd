from my_project.auth.dao.gereral_dao import GeneralDAO
from my_project.auth.domain.reservation.reservation_time import ReservationTime


class ReservationTimeDao(GeneralDAO):
    _domain_type = ReservationTime