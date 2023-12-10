from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify

from my_project import db
from my_project.auth.controller import people_controller
from my_project.auth.domain.people.people import People

people_bp = Blueprint("people", __name__, url_prefix="/people/")

@people_bp.route("", methods=["GET"])
def get_all_people() -> Response:
    return make_response(jsonify(people_controller.find_all()), HTTPStatus.OK)

@people_bp.route('/<int:people_id>', methods=["GET"])
def get_people(people_id: int) -> Response:
    return make_response(jsonify(people_controller.find_by_id(people_id)), HTTPStatus.OK)

@people_bp.route('/<int:people_id>',  methods=["PUT"])
def update_people(people_id: int) -> Response:
    content = request.get_json()
    people = People.create_from_dto(content)
    people_controller.update(people_id, people)
    return make_response("People Updated", HTTPStatus.OK)

@people_bp.route('/<int:people_id>', methods=["PATCH"])
def patch_people(people_id: int) -> Response:
    content = request.get_json()
    people_controller.patch(people_id, content)
    return make_response("People Updated", HTTPStatus.OK)

@people_bp.route('/<int:people_id>', methods=["DELETE"])
def delete_people(people_id: int) -> Response:
    people_controller.delete(people_id)
    return make_response("People deleted", HTTPStatus.OK)

@people_bp.route('', methods=["POST"])
def create_people() -> Response:
    content = request.get_json()
    people = People.create_from_dto(content)
    people_id = people_controller.create(people)
    return make_response(f"People with id {people_id} created", HTTPStatus.CREATED)

@people_bp.route('/bulk', methods=["POST"])
def create_all_people() -> Response:
    content = request.get_json()
    people = [People.create_from_dto(data) for data in content]
    people_controller.create_all(people)
    return make_response(people_controller.create_all(people), HTTPStatus.CREATED)

@people_bp.route("/all", methods=["DELETE"])
def delete_all_people() -> Response:
    people_controller.delete_all()
    return make_response("All people deleted", HTTPStatus.OK)

