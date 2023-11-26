from base_servise import BaseService
from domain.people import Persone

class PeopleService(BaseService):
    def create_item(self, data):
        return Persone(first_name=data["first_name"], last_name=data["last_name"])
