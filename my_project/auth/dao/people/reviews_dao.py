from my_project.auth.dao.gereral_dao import GeneralDAO
from my_project.auth.domain.people.reviews import Reviews


class ReviewsDao(GeneralDAO):
    _domain_type = Reviews