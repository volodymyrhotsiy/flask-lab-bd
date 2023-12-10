from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify

from my_project import db
from my_project.auth.controller import reservation_history_controller
from my_project.auth.domain.reservation.reservation_history import ReservationHistory

reservation_history_bp = Blueprint("reservation_history", __name__, url_prefix="/reservation_history/")

@reservation_history_bp.route("", methods=["GET"])
def get_all_reservation_history() -> Response:
    return make_response(jsonify(reservation_history_controller.find_all()), HTTPStatus.OK)

@reservation_history_bp.route('/<int:reservation_history_id>', methods=["GET"])
def get_reservation_history(reservation_history_id: int) -> Response:
    return make_response(jsonify(reservation_history_controller.find_by_id(reservation_history_id)), HTTPStatus.OK)

@reservation_history_bp.route('/<int:reservation_history_id>', methods=["PUT"])
def update_reservation_history(reservation_history_id: int) -> Response:
    content = request.get_json()
    reservation_history = ReservationHistory.create_from_dto(content)
    reservation_history_controller.update(reservation_history_id, reservation_history)
    return make_response("ReservationHistory Updated", HTTPStatus.OK)

@reservation_history_bp.route('/<int:reservation_history_id>', methods=["PATCH"])
def patch_reservation_history(reservation_history_id: int) -> Response:
    content = request.get_json()
    reservation_history_controller.patch(reservation_history_id, content)
    return make_response("ReservationHistory Updated", HTTPStatus.OK)

@reservation_history_bp.route('/<int:reservation_history_id>', methods=["DELETE"])
def delete_reservation_history(reservation_history_id: int) -> Response:
    reservation_history_controller.delete(reservation_history_id)
    return make_response("ReservationHistory deleted", HTTPStatus.OK)

@reservation_history_bp.route('', methods=["POST"])
def create_reservation_history() -> Response:
    content = request.get_json()
    reservation_history = ReservationHistory.create_from_dto(content)
    reservation_history_id = reservation_history_controller.create(reservation_history)
    return make_response(f"ReservationHistory with id {reservation_history_id} created", HTTPStatus.CREATED)

@reservation_history_bp.route('/bulk', methods=["POST"])
def create_all_reservation_history() -> Response:
    content = request.get_json()
    reservation_history = [ReservationHistory.create_from_dto(data) for data in content]
    reservation_history_controller.create_all(reservation_history)
    return make_response(reservation_history_controller.create_all(reservation_history), HTTPStatus.CREATED)

@reservation_history_bp.route("/all", methods=["DELETE"])
def delete_all_reservation_history() -> Response:
    reservation_history_controller.delete_all()
    return make_response("All ReservationHistory deleted", HTTPStatus.OK)

