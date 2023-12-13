from my_project.auth.dao import people_dao
from my_project.auth.service.general_service import GeneralService
from flask import abort
from http import HTTPStatus


class PeopleService(GeneralService):
    _dao = people_dao

    def get_people_photos(self, id: int):
        people = self._dao.find_by_id(id)
        if not people:
            abort(HTTPStatus.NOT_FOUND)

        return people.photos
    
    def get_reviews(self, id: int):
        people = self._dao.find_by_id(id)
        if not people:
            abort(HTTPStatus.NOT_FOUND)

        return people.reviews

    def get_property(self, id: int):
        people = self._dao.find_by_id(id)
        if not people:
            abort(HTTPStatus.NOT_FOUND)

        return people.property   

    def get_reservation(self, id: int):
        people = self._dao.find_by_id(id)
        if not people:
            abort(HTTPStatus.NOT_FOUND)

        return people.reservation    