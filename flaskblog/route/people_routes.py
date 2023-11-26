from base_route_blueprint import BaseRouteBlueprint
from controller.people_controller import (
    add_people_route,
    get_people_route,
    get_people_by_id_route,
    edit_people_route,
    delete_people_route,
)

class PeopleRouteBlueprint(BaseRouteBlueprint):
    def __init__(self):
        super().__init__("people", __name__)

        self.add_route("/people", ["POST"], add_people_route)
        self.add_route("/people", ["GET"], get_people_route)
        self.add_route("/people/<int:people_id>", ["GET"], get_people_by_id_route)
        self.add_route("/people/<int:people_id>", ["PUT"], edit_people_route)
        self.add_route("/people/<int:people_id>", ["DELETE"], delete_people_route)

people_bp = PeopleRouteBlueprint()
