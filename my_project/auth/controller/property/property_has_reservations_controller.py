from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import property_has_reservations_service

class PropertyHasReservationsController(GeneralController):
    _service = property_has_reservations_service

    def get_properties_for_reservation(self, id: int):
        return [property.put_into_dto() for property in self._service.get_properties_for_reservation(id)]

    def get_reservations_for_property(self, id: int):
        return [reservation.put_into_dto() for reservation in self._service.get_reservations_for_property(id)]
