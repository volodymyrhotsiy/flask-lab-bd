from my_project.auth.dao.gereral_dao import GeneralDAO
from my_project.auth.domain.people.people_photos import PeoplePhotos


class PeoplePhotosDao(GeneralDAO):
    _domain_type = PeoplePhotos