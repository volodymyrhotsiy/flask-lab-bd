from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import reviews_service


class ReviewsController(GeneralController):
    _service = reviews_service