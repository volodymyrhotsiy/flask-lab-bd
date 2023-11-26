from base_route_blueprint import BaseRouteBlueprint
from controller.address_controller import (
    add_address_route,
    get_address_route,
    get_address_by_id_route,
    edit_address_route,
    delete_address_route,
)

class AddressRouteBlueprint(BaseRouteBlueprint):
    def __init__(self):
        super().__init__("address", __name__)

        self.add_route("/address", ["POST"], add_address_route)
        self.add_route("/address", ["GET"], get_address_route)
        self.add_route("/address/<int:address_id>", ["GET"], get_address_by_id_route)
        self.add_route("/address/<int:address_id>", ["PUT"], edit_address_route)
        self.add_route("/address/<int:address_id>", ["DELETE"], delete_address_route)

address_bp = AddressRouteBlueprint()
