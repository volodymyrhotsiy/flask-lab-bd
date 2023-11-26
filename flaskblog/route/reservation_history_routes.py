from base_route_blueprint import BaseRouteBlueprint
from controller.reservation_history_controller import (
    add_reservation_history_route,
    get_reservation_history_route,
    get_reservation_history_by_id_route,
    edit_reservation_history_route,
    delete_reservation_history_route,
)

class ReservationHistoryRouteBlueprint(BaseRouteBlueprint):
    def __init__(self):
        super().__init__("reservation_history", __name__)

        self.add_route("/reservation_history", ["POST"], add_reservation_history_route)
        self.add_route("/reservation_history", ["GET"], get_reservation_history_route)
        self.add_route("/reservation_history/<int:reservation_history_id>", ["GET"], get_reservation_history_by_id_route)
        self.add_route("/reservation_history/<int:reservation_history_id>", ["PUT"], edit_reservation_history_route)
        self.add_route("/reservation_history/<int:reservation_history_id>", ["DELETE"], delete_reservation_history_route)

reservation_history_bp = ReservationHistoryRouteBlueprint()
