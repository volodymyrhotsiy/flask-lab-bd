from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify
from my_project.auth.controller import people_photos_controller
from my_project.auth.domain.people.people_photos import PeoplePhotos

people_photos_bp = Blueprint("people_photos", __name__, url_prefix="/people_photos/")

@people_photos_bp.route("",  methods=["GET"])
def get_all_people_photos() -> Response:
    return make_response(jsonify(people_photos_controller.find_all()), HTTPStatus.OK)

@people_photos_bp.route('/<int:people_photos_id>', methods=["GET"])
def get_people_photos(people_photos_id: int) -> Response:
    return make_response(jsonify(people_photos_controller.find_by_id(people_photos_id)), HTTPStatus.OK)

@people_photos_bp.route('/<int:people_photos_id>', methods=["PUT"])
def update_people_photos(people_photos_id: int) -> Response:
    content = request.get_json()
    people_photos = PeoplePhotos.create_from_dto(content)
    people_photos_controller.update(people_photos_id, people_photos)
    return make_response("PeoplePhotos Updated", HTTPStatus.OK)

@people_photos_bp.route('/<int:people_photos_id>', methods=["PATCH"])
def patch_people_photos(people_photos_id: int) -> Response:
    content = request.get_json()
    people_photos_controller.patch(people_photos_id, content)
    return make_response("PeoplePhotos Updated", HTTPStatus.OK)

@people_photos_bp.route('/<int:people_photos_id>', methods=["DELETE"])
def delete_people_photos(people_photos_id: int) -> Response:
    people_photos_controller.delete(people_photos_id)
    return make_response("PeoplePhotos deleted", HTTPStatus.OK)

@people_photos_bp.route('', methods=["POST"])
def create_people_photos() -> Response:
    content = request.get_json()
    people_photos = PeoplePhotos.create_from_dto(content)
    people_photos_id = people_photos_controller.create(people_photos)
    return make_response(f"PeoplePhotos with id {people_photos_id} created", HTTPStatus.CREATED)

@people_photos_bp.route('/bulk', methods=["POST"])
def create_all_people_photos() -> Response:
    content = request.get_json()
    people_photos = [PeoplePhotos.create_from_dto(data) for data in content]
    people_photos_controller.create_all(people_photos)
    return make_response(people_photos_controller.create_all(people_photos), HTTPStatus.CREATED)

@people_photos_bp.route("/all", methods=["DELETE"])
def delete_all_people_photos() -> Response:
    people_photos_controller.delete_all()
    return make_response("All peoplePhotos deleted", HTTPStatus.OK)

