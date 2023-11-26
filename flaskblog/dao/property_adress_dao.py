from domain.property_adress import PropertyAdress
from base_dao import BaseDAO

class PropertyAdressDAO(BaseDAO):
    model = PropertyAdress

    def _serialize(self, property_adress):
        return {
            "id": property_adress.id,
            "state": property_adress.state,
            "street": property_adress.street,
            "street_number": property_adress.street_number
        }

    def _update_item(self, property_adress, data):
        property_adress.state = data.get("state", property_adress.state)
        property_adress.street = data.get("street", property_adress.street)
        property_adress.street_number = data.get("street_number", property_adress.street_number)
