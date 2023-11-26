from base_servise import BaseService
from domain.review import Review

class ReviewService(BaseService):
    def create_item(self, data):
        return Review(
            rating=data["rating"],
            comment=data["comment"],
            review_date=data["review_date"],
            person_id=data["person_id"],
        )