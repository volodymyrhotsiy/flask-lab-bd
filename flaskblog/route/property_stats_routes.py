from base_route_blueprint import BaseRouteBlueprint
from controller.property_stats_controller import (
    add_property_stats_route,
    get_property_stats_route,
    get_property_stats_by_id_route,
    edit_property_stats_route,
    delete_property_stats_route,
)

class PropertyStatsRouteBlueprint(BaseRouteBlueprint):
    def __init__(self):
        super().__init__("property_stats", __name__)

        self.add_route("/property_stats", ["POST"], add_property_stats_route)
        self.add_route("/property_stats", ["GET"], get_property_stats_route)
        self.add_route("/property_stats/<int:property_stats_id>", ["GET"], get_property_stats_by_id_route)
        self.add_route("/property_stats/<int:property_stats_id>", ["PUT"], edit_property_stats_route)
        self.add_route("/property_stats/<int:property_stats_id>", ["DELETE"], delete_property_stats_route)

property_stats_bp = PropertyStatsRouteBlueprint()
