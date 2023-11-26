from base_servise import BaseService
from domain.property import Property

class PropertyService(BaseService):
    def create_item(self, data):
        return Property(
            person_id=data["person_id"],
            property_stats=data["property_stats"],
            property_adress=data["property_adress"],
        )