from base_route_blueprint import BaseRouteBlueprint
from controller.reservation_time_controller import (
    add_reservation_time_route,
    get_reservation_time_route,
    get_reservation_time_by_id_route,
    edit_reservation_time_route,
    delete_reservation_time_route,
)

class ReservationTimeRouteBlueprint(BaseRouteBlueprint):
    def __init__(self):
        super().__init__("reservation_time", __name__)

        self.add_route("/reservation_time", ["POST"], add_reservation_time_route)
        self.add_route("/reservation_time", ["GET"], get_reservation_time_route)
        self.add_route("/reservation_time/<int:reservation_time_id>", ["GET"], get_reservation_time_by_id_route)
        self.add_route("/reservation_time/<int:reservation_time_id>", ["PUT"], edit_reservation_time_route)
        self.add_route("/reservation_time/<int:reservation_time_id>", ["DELETE"], delete_reservation_time_route)

reservation_time_bp = ReservationTimeRouteBlueprint()
