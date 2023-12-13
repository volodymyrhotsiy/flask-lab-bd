from my_project.auth.dao import property_has_reservations_dao
from my_project.auth.service.general_service import GeneralService

from flask import abort
from http import HTTPStatus

class PropertyHasReservationsService(GeneralService):
    _dao = property_has_reservations_dao

    def get_properties_for_reservation(self, reservation_id: int):
        properties = self._dao.find_properties_by_reservation_id(reservation_id)
        if not properties:
            abort(HTTPStatus.NOT_FOUND)

        return properties

    def get_reservations_for_property(self, property_id: int):
        reservations = self._dao.find_reservations_by_property_id(property_id)
        if not reservations:
            abort(HTTPStatus.NOT_FOUND)

        return reservations