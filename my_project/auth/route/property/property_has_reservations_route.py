from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify

from my_project import db
from my_project.auth.controller import property_has_reservations_controller
from my_project.auth.domain.property.property_has_reservations import PropertyHasReservations

property_has_reservations_bp = Blueprint("property_has_reservations", __name__, url_prefix="/property_has_reservations/")

@property_has_reservations_bp.route("", methods=["GET"])
def get_all_property_has_reservations() -> Response:
    return make_response(jsonify(property_has_reservations_controller.find_all()), HTTPStatus.OK)

@property_has_reservations_bp.route('/<int:property_has_reservations_id>', methods=["GET"])
def get_property_has_reservations(property_has_reservations_id: int) -> Response:
    return make_response(jsonify(property_has_reservations_controller.find_by_id(property_has_reservations_id)), HTTPStatus.OK)

@property_has_reservations_bp.route('/<int:property_has_reservations_id>', methods=["PUT"])
def update_property_has_reservations(property_has_reservations_id: int) -> Response:
    content = request.get_json()
    property_has_reservations = PropertyHasReservations.create_from_dto(content)
    property_has_reservations_controller.update(property_has_reservations_id, property_has_reservations)
    return make_response("PropertyHasReservations Updated", HTTPStatus.OK)

@property_has_reservations_bp.route('/<int:property_has_reservations_id>', methods=["PATCH"])
def patch_property_has_reservations(property_has_reservations_id: int) -> Response:
    content = request.get_json()
    property_has_reservations_controller.patch(property_has_reservations_id, content)
    return make_response("PropertyHasReservations Updated", HTTPStatus.OK)

@property_has_reservations_bp.route('/<int:property_has_reservations_id>', methods=["DELETE"])
def delete_property_has_reservations(property_has_reservations_id: int) -> Response:
    property_has_reservations_controller.delete(property_has_reservations_id)
    return make_response("PropertyHasReservations deleted", HTTPStatus.OK)

@property_has_reservations_bp.route('', methods=["POST"])
def create_property_has_reservations() -> Response:
    content = request.get_json()
    property_has_reservations = PropertyHasReservations.create_from_dto(content)
    property_has_reservations_id = property_has_reservations_controller.create(property_has_reservations)
    return make_response(f"PropertyHasReservations with id {property_has_reservations_id} created", HTTPStatus.CREATED)

@property_has_reservations_bp.route('/bulk', methods=["POST"])
def create_all_property_has_reservations() -> Response:
    content = request.get_json()
    property_has_reservations = [PropertyHasReservations.create_from_dto(data) for data in content]
    property_has_reservations_controller.create_all(property_has_reservations)
    return make_response(property_has_reservations_controller.create_all(property_has_reservations), HTTPStatus.CREATED)

@property_has_reservations_bp.route("/all", methods=["DELETE"])
def delete_all_property_has_reservations() -> Response:
    property_has_reservations_controller.delete_all()
    return make_response("All PropertyHasReservations deleted", HTTPStatus.OK)

@property_has_reservations_bp.route("/property/<int:property_id>", methods=["GET"])
def get_properties_for_reservation(property_id: int) -> Response:
    return make_response(jsonify(property_has_reservations_controller.get_reservations_for_property(property_id)), HTTPStatus.OK)

@property_has_reservations_bp.route("/reservation/<int:reservation_id>", methods=["GET"])
def get_reservations_for_property(reservation_id: int) -> Response:
    return make_response(jsonify(property_has_reservations_controller.get_properties_for_reservation(reservation_id)), HTTPStatus.OK)

