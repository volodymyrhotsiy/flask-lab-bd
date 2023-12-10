from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import property_has_reservations_service


class PropertyHasReservationsController(GeneralController):
    _service = property_has_reservations_service