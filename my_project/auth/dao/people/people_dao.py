from my_project.auth.dao.gereral_dao import GeneralDAO
from my_project.auth.domain.people.people import People


class PeopleDao(GeneralDAO):
    _domain_type = People