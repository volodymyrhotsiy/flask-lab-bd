from my_project.auth.dao import reviews_dao
from my_project.auth.service.general_service import GeneralService


class ReviewsService(GeneralService):
    _dao = reviews_dao