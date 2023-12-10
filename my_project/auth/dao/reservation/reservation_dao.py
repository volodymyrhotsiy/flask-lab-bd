from my_project.auth.dao.gereral_dao import GeneralDAO
from my_project.auth.domain.reservation.reservation import Reservation


class ReservationDao(GeneralDAO):
    _domain_type = Reservation