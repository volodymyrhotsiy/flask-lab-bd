from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify

from my_project import db
from my_project.auth.controller import property_controller
from my_project.auth.domain.property.property import Property

property_bp = Blueprint("property", __name__, url_prefix="/property/")

@property_bp.route("", methods=["GET"])
def get_all_property() -> Response:
    return make_response(jsonify(property_controller.find_all()), HTTPStatus.OK)

@property_bp.route('/<int:property_id>', methods=["GET"])
def get_property(property_id: int) -> Response:
    return make_response(jsonify(property_controller.find_by_id(property_id)), HTTPStatus.OK)

@property_bp.route('/<int:property_id>', methods=["PUT"])
def update_property(property_id: int) -> Response:
    content = request.get_json()
    property = Property.create_from_dto(content)
    property_controller.update(property_id, property)
    return make_response("Property Updated", HTTPStatus.OK)

@property_bp.route('/<int:property_id>', methods=["PATCH"])
def patch_property(property_id: int) -> Response:
    content = request.get_json()
    property_controller.patch(property_id, content)
    return make_response("Property Updated", HTTPStatus.OK)

@property_bp.route('/<int:property_id>', methods=["DELETE"])
def delete_property(property_id: int) -> Response:
    property_controller.delete(property_id)
    return make_response("Property deleted", HTTPStatus.OK)

@property_bp.route('', methods=["POST"])
def create_property() -> Response:
    content = request.get_json()
    property = Property.create_from_dto(content)
    property_id = property_controller.create(property)
    return make_response(f"Property with id {property_id} created", HTTPStatus.CREATED)

@property_bp.route('/bulk', methods=["POST"])
def create_all_property() -> Response:
    content = request.get_json()
    property = [Property.create_from_dto(data) for data in content]
    property_controller.create_all(property)
    return make_response(property_controller.create_all(property), HTTPStatus.CREATED)

@property_bp.route("/all", methods=["DELETE"])
def delete_all_property() -> Response:
    property_controller.delete_all()
    return make_response("All Property deleted", HTTPStatus.OK)

