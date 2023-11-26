from base_route_blueprint import BaseRouteBlueprint
from controller.reservation_controller import (
    add_reservation_route,
    get_reservation_route,
    get_reservation_by_id_route,
    edit_reservation_route,
    delete_reservation_route,
)

class ReservationRouteBlueprint(BaseRouteBlueprint):
    def __init__(self):
        super().__init__("reservation", __name__)

        self.add_route("/reservation", ["POST"], add_reservation_route)
        self.add_route("/reservation", ["GET"], get_reservation_route)
        self.add_route("/reservation/<int:reservation_id>", ["GET"], get_reservation_by_id_route)
        self.add_route("/reservation/<int:reservation_id>", ["PUT"], edit_reservation_route)
        self.add_route("/reservation/<int:reservation_id>", ["DELETE"], delete_reservation_route)

reservation_bp = ReservationRouteBlueprint()
