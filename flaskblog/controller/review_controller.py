from base_controller import BaseController
from service.review_service import ReviewService

class ReviewController(BaseController):
    def __init__(self):
        super().__init__(ReviewService())