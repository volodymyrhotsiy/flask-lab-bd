from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify

from my_project import db
from my_project.auth.controller import reservation_controller
from my_project.auth.domain.reservation.reservation import Reservation

reservation_bp = Blueprint("reservation", __name__, url_prefix="/reservation/")

@reservation_bp.route("", methods=["GET"])
def get_all_reservation() -> Response:
    return make_response(jsonify(reservation_controller.find_all()), HTTPStatus.OK)

@reservation_bp.route('/<int:reservation_id>', methods=["GET"])
def get_reservation(reservation_id: int) -> Response:
    return make_response(jsonify(reservation_controller.find_by_id(reservation_id)), HTTPStatus.OK)

@reservation_bp.route('/<int:reservation_id>', methods=["PUT"])
def update_reservation(reservation_id: int) -> Response:
    content = request.get_json()
    reservation = Reservation.create_from_dto(content)
    reservation_controller.update(reservation_id, reservation)
    return make_response("Reservation Updated", HTTPStatus.OK)

@reservation_bp.route('/<int:reservation_id>', methods=["PATCH"])
def patch_reservation(reservation_id: int) -> Response:
    content = request.get_json()
    reservation_controller.patch(reservation_id, content)
    return make_response("Reservation Updated", HTTPStatus.OK)

@reservation_bp.route('/<int:reservation_id>', methods=["DELETE"])
def delete_reservation(reservation_id: int) -> Response:
    reservation_controller.delete(reservation_id)
    return make_response("Reservation deleted", HTTPStatus.OK)

@reservation_bp.route('', methods=["POST"])
def create_reservation() -> Response:
    content = request.get_json()
    reservation = Reservation.create_from_dto(content)
    reservation_id = reservation_controller.create(reservation)
    return make_response(f"Reservation with id {reservation_id} created", HTTPStatus.CREATED)

@reservation_bp.route('/bulk', methods=["POST"])
def create_all_reservation() -> Response:
    content = request.get_json()
    reservation = [Reservation.create_from_dto(data) for data in content]
    reservation_controller.create_all(reservation)
    return make_response(reservation_controller.create_all(reservation), HTTPStatus.CREATED)

@reservation_bp.route("/all", methods=["DELETE"])
def delete_all_reservation() -> Response:
    reservation_controller.delete_all()
    return make_response("All Reservation deleted", HTTPStatus.OK)

