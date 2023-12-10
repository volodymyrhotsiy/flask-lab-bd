from my_project.auth.dao import reservation_time_dao
from my_project.auth.service.general_service import GeneralService


class ReservationTimeService(GeneralService):
    _dao = reservation_time_dao