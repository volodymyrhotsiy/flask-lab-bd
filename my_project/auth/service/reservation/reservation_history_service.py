from my_project.auth.dao import reservation_history_dao
from my_project.auth.service.general_service import GeneralService


class ReservationHistoryService(GeneralService):
    _dao = reservation_history_dao