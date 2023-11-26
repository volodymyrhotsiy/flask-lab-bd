from domain.review import Review
from base_dao import BaseDAO

class ReviewDAO(BaseDAO):
    model = Review

    def _serialize(self, review):
        return {
            "id": review.id,
            "rating": review.rating,
            "comment": review.comment,
            "review_date": review.review_date,
            "person_id": review.person_id
        }

    def _update_item(self, review, data):
        review.rating = data.get("rating", review.rating)
        review.comment = data.get("comment", review.comment)
