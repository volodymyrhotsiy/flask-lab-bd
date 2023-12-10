from my_project.auth.dao.gereral_dao import GeneralDAO
from my_project.auth.domain.property.property_has_reservations import PropertyHasReservations


class PropertyHasReservationsDao(GeneralDAO):
    _domain_type = PropertyHasReservations