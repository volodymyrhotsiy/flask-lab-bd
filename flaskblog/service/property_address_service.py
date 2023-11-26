from base_servise import BaseService
from domain.property_adress import PropertyAdress

class PropertyAdressService(BaseService):
    def create_item(self, data):
        return PropertyAdress(state=data["state"], street=data["street"], street_number=data["street_number"])