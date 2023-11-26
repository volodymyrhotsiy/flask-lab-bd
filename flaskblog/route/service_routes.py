from base_route_blueprint import BaseRouteBlueprint
from controller.service_controller import (
    add_service_route,
    get_service_route,
    get_service_by_id_route,
    edit_service_route,
    delete_service_route,
)

class ServiceRouteBlueprint(BaseRouteBlueprint):
    def __init__(self):
        super().__init__("service", __name__)

        self.add_route("/service", ["POST"], add_service_route)
        self.add_route("/service", ["GET"], get_service_route)
        self.add_route("/service/<int:service_id>", ["GET"], get_service_by_id_route)
        self.add_route("/service/<int:service_id>", ["PUT"], edit_service_route)
        self.add_route("/service/<int:service_id>", ["DELETE"], delete_service_route)

service_bp = ServiceRouteBlueprint()
