from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify

from my_project import db
from my_project.auth.controller import reservation_time_controller
from my_project.auth.domain.reservation.reservation_time import ReservationTime

reservation_time_bp = Blueprint("reservation_time", __name__, url_prefix="/reservation_time/")

@reservation_time_bp.route("", methods=["GET"])
def get_all_reservation_time() -> Response:
    return make_response(jsonify(reservation_time_controller.find_all()), HTTPStatus.OK)

@reservation_time_bp.route('/<int:reservation_time_id>', methods=["GET"])
def get_reservation_time(reservation_time_id: int) -> Response:
    return make_response(jsonify(reservation_time_controller.find_by_id(reservation_time_id)), HTTPStatus.OK)

@reservation_time_bp.route('/<int:reservation_time_id>', methods=["PUT"])
def update_reservation_time(reservation_time_id: int) -> Response:
    content = request.get_json()
    reservation_time = ReservationTime.create_from_dto(content)
    reservation_time_controller.update(reservation_time_id, reservation_time)
    return make_response("ReservationTime Updated", HTTPStatus.OK)

@reservation_time_bp.route('/<int:reservation_time_id>', methods=["PATCH"])
def patch_reservation_time(reservation_time_id: int) -> Response:
    content = request.get_json()
    reservation_time_controller.patch(reservation_time_id, content)
    return make_response("ReservationTime Updated", HTTPStatus.OK)

@reservation_time_bp.route('/<int:reservation_time_id>', methods=["DELETE"])
def delete_reservation_time(reservation_time_id: int) -> Response:
    reservation_time_controller.delete(reservation_time_id)
    return make_response("ReservationTime deleted", HTTPStatus.OK)

@reservation_time_bp.route('', methods=["POST"])
def create_reservation_time() -> Response:
    content = request.get_json()
    reservation_time = ReservationTime.create_from_dto(content)
    reservation_time_id = reservation_time_controller.create(reservation_time)
    return make_response(f"ReservationTime with id {reservation_time_id} created", HTTPStatus.CREATED)

@reservation_time_bp.route('/bulk', methods=["POST"])
def create_all_reservation_time() -> Response:
    content = request.get_json()
    reservation_time = [ReservationTime.create_from_dto(data) for data in content]
    reservation_time_controller.create_all(reservation_time)
    return make_response(reservation_time_controller.create_all(reservation_time), HTTPStatus.CREATED)

@reservation_time_bp.route("/all", methods=["DELETE"])
def delete_all_reservation_time() -> Response:
    reservation_time_controller.delete_all()
    return make_response("All ReservationTime deleted", HTTPStatus.OK)

