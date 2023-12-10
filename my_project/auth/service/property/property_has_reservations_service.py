from my_project.auth.dao import property_has_reservations_dao
from my_project.auth.service.general_service import GeneralService


class PropertyHasReservationsService(GeneralService):
    _dao = property_has_reservations_dao