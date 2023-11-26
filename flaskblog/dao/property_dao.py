from domain.property import Property
from base_dao import BaseDAO

class PropertyDAO(BaseDAO):
    model = Property

    def _serialize(self, prop):
        return {
            "id": prop.id,
            "person_id": prop.person_id,
            "property_stats": prop.property_stats,
            "property_adress": prop.property_adress
        }

    def _update_item(self, prop, data):
        prop.person_id = data.get("person_id", prop.person_id)
        prop.property_stats = data.get("property_stats", prop.property_stats)
        prop.property_adress = data.get("property_adress", prop.property_adress)