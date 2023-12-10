from my_project.auth.dao import reservation_dao
from my_project.auth.service.general_service import GeneralService


class ReservationService(GeneralService):
    _dao = reservation_dao