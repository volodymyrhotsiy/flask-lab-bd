from base_route_blueprint import BaseRouteBlueprint
from controller.photo_controller import (
    add_photo_route,
    get_photo_route,
    get_photo_by_id_route,
    edit_photo_route,
    delete_photo_route,
)

class PhotoRouteBlueprint(BaseRouteBlueprint):
    def __init__(self):
        super().__init__("photo", __name__)

        self.add_route("/photo", ["POST"], add_photo_route)
        self.add_route("/photo", ["GET"], get_photo_route)
        self.add_route("/photo/<int:photo_id>", ["GET"], get_photo_by_id_route)
        self.add_route("/photo/<int:photo_id>", ["PUT"], edit_photo_route)
        self.add_route("/photo/<int:photo_id>", ["DELETE"], delete_photo_route)

photo_bp = PhotoRouteBlueprint()
