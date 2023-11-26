from base_route_blueprint import BaseRouteBlueprint
from controller.review_controller import (
    add_review_route,
    get_review_route,
    get_review_by_id_route,
    edit_review_route,
    delete_review_route,
)

class ReviewRouteBlueprint(BaseRouteBlueprint):
    def __init__(self):
        super().__init__("review", __name__)

        self.add_route("/review", ["POST"], add_review_route)
        self.add_route("/review", ["GET"], get_review_route)
        self.add_route("/review/<int:review_id>", ["GET"], get_review_by_id_route)
        self.add_route("/review/<int:review_id>", ["PUT"], edit_review_route)
        self.add_route("/review/<int:review_id>", ["DELETE"], delete_review_route)

review_bp = ReviewRouteBlueprint()
