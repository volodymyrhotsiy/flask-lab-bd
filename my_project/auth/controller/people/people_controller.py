from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import people_service


class PeopleController(GeneralController):
    _service = people_service

    def get_people_photos(self, id: int):
        return[people_photo.put_into_dto() for people_photo in self._service.get_people_photos(id)]
    
    def get_reviews(self, id: int):
        return[review.put_into_dto() for review in self._service.get_reviews(id)]
    
    def get_property(self, id: int):
        return[property.put_into_dto() for property in self._service.get_property(id)]
    
    def get_reservation(self, id: int):
        return[reservation.put_into_dto() for reservation in self._service.get_reservation(id)]