from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify

from my_project import db
from my_project.auth.controller import property_stats_controller
from my_project.auth.domain.property.property_stats import PropertyStats

property_stats_bp = Blueprint("property_stats", __name__, url_prefix="/property_stats/")

@property_stats_bp.route("", methods=["GET"])
def get_all_property_stats() -> Response:
    return make_response(jsonify(property_stats_controller.find_all()), HTTPStatus.OK)

@property_stats_bp.route('/<int:property_stats_id>', methods=["GET"])
def get_property_stats(property_stats_id: int) -> Response:
    return make_response(jsonify(property_stats_controller.find_by_id(property_stats_id)), HTTPStatus.OK)

@property_stats_bp.route('/<int:property_stats_id>', methods=["PUT"])
def update_property_stats(property_stats_id: int) -> Response:
    content = request.get_json()
    property_stats = PropertyStats.create_from_dto(content)
    property_stats_controller.update(property_stats_id, property_stats)
    return make_response("PropertyStats Updated", HTTPStatus.OK)

@property_stats_bp.route('/<int:property_stats_id>', methods=["PATCH"])
def patch_property_stats(property_stats_id: int) -> Response:
    content = request.get_json()
    property_stats_controller.patch(property_stats_id, content)
    return make_response("PropertyStats Updated", HTTPStatus.OK)

@property_stats_bp.route('/<int:property_stats_id>', methods=["DELETE"])
def delete_property_stats(property_stats_id: int) -> Response:
    property_stats_controller.delete(property_stats_id)
    return make_response("PropertyStats deleted", HTTPStatus.OK)

@property_stats_bp.route('', methods=["POST"])
def create_property_stats() -> Response:
    content = request.get_json()
    property_stats = PropertyStats.create_from_dto(content)
    property_stats_id = property_stats_controller.create(property_stats)
    return make_response(f"PropertyStats with id {property_stats_id} created", HTTPStatus.CREATED)

@property_stats_bp.route('/bulk', methods=["POST"])
def create_all_property_stats() -> Response:
    content = request.get_json()
    property_stats = [PropertyStats.create_from_dto(data) for data in content]
    property_stats_controller.create_all(property_stats)
    return make_response(property_stats_controller.create_all(property_stats), HTTPStatus.CREATED)

@property_stats_bp.route("/all", methods=["DELETE"])
def delete_all_property_stats() -> Response:
    property_stats_controller.delete_all()
    return make_response("All PropertyStats deleted", HTTPStatus.OK)

