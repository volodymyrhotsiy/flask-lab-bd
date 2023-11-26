from base_route_blueprint import BaseRouteBlueprint
from controller.property_controller import (
    add_property_route,
    get_property_route,
    get_property_by_id_route,
    edit_property_route,
    delete_property_route,
)

class PropertyRouteBlueprint(BaseRouteBlueprint):
    def __init__(self):
        super().__init__("property", __name__)

        self.add_route("/property", ["POST"], add_property_route)
        self.add_route("/property", ["GET"], get_property_route)
        self.add_route("/property/<int:property_id>", ["GET"], get_property_by_id_route)
        self.add_route("/property/<int:property_id>", ["PUT"], edit_property_route)
        self.add_route("/property/<int:property_id>", ["DELETE"], delete_property_route)

property_bp = PropertyRouteBlueprint()
