from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify

from my_project import db
from my_project.auth.controller import address_controller
from my_project.auth.domain.property.address import Address
address_bp = Blueprint("address", __name__, url_prefix="/address/")

@address_bp.route("", methods=["GET"])
def get_all_address() -> Response:
    return make_response(jsonify(address_controller.find_all()), HTTPStatus.OK)

@address_bp.route('/<int:address_id>', methods=["GET"])
def get_address(address_id: int) -> Response:
    return make_response(jsonify(address_controller.find_by_id(address_id)), HTTPStatus.OK)

@address_bp.route('/<int:address_id>', methods=["PUT"])
def update_address(address_id: int) -> Response:
    content = request.get_json()
    address = Address.create_from_dto(content)
    address_controller.update(address_id, address)
    return make_response("Address Updated", HTTPStatus.OK)

@address_bp.route('/<int:address_id>', methods=["PATCH"])
def patch_address(address_id: int) -> Response:
    content = request.get_json()
    address_controller.patch(address_id, content)
    return make_response("Address Updated", HTTPStatus.OK)

@address_bp.route('/<int:address_id>', methods=["DELETE"])
def delete_address(address_id: int) -> Response:
    address_controller.delete(address_id)
    return make_response("Address deleted", HTTPStatus.OK)

@address_bp.route('', methods=["POST"])
def create_address() -> Response:
    content = request.get_json()
    address = Address.create_from_dto(content)
    address_id = address_controller.create(address)
    return make_response(f"Address with id {address_id} created", HTTPStatus.CREATED)

@address_bp.route('/bulk', methods=["POST"])
def create_all_address() -> Response:
    content = request.get_json()
    address = [Address.create_from_dto(data) for data in content]
    address_controller.create_all(address)
    return make_response(address_controller.create_all(address), HTTPStatus.CREATED)

@address_bp.route("/all", methods=["DELETE"])
def delete_all_address() -> Response:
    address_controller.delete_all()
    return make_response("All Address deleted", HTTPStatus.OK)

