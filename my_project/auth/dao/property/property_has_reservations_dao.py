from my_project.auth.dao.gereral_dao import GeneralDAO
from my_project.auth.domain.property.property_has_reservations import PropertyHasReservations
from typing import List

class PropertyHasReservationsDao(GeneralDAO):
    _domain_type = PropertyHasReservations

    def find_reservations_by_property_id(self, property_id: int) -> List[PropertyHasReservations]:
        return self._session.query(self._domain_type).filter_by(property_id=property_id).all()

    def find_properties_by_reservation_id(self, reservation_id: int) -> List[PropertyHasReservations]:
        return self._session.query(self._domain_type).filter_by(reservation_id=reservation_id).all()
