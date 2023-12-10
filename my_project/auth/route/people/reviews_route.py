from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify

from my_project import db
from my_project.auth.controller import reviews_controller
from my_project.auth.domain.people.reviews import Reviews

reviews_bp = Blueprint("reviews", __name__, url_prefix="/reviews/")

@reviews_bp.route("", methods=["GET"])
def get_all_reviews() -> Response:
    return make_response(jsonify(reviews_controller.find_all()), HTTPStatus.OK)

@reviews_bp.route('/<int:reviews_id>', methods=["GET"])
def get_reviews(reviews_id: int) -> Response:
    return make_response(jsonify(reviews_controller.find_by_id(reviews_id)), HTTPStatus.OK)

@reviews_bp.route('/<int:reviews_id>', methods=["PUT"])
def update_reviews(reviews_id: int) -> Response:
    content = request.get_json()
    reviews = Reviews.create_from_dto(content)
    reviews_controller.update(reviews_id, reviews)
    return make_response("Reviews Updated", HTTPStatus.OK)

@reviews_bp.route('/<int:reviews_id>', methods=["PATCH"])
def patch_reviews(reviews_id: int) -> Response:
    content = request.get_json()
    reviews_controller.patch(reviews_id, content)
    return make_response("Reviews Updated", HTTPStatus.OK)

@reviews_bp.route('/<int:reviews_id>', methods=["DELETE"])
def delete_reviews(reviews_id: int) -> Response:
    reviews_controller.delete(reviews_id)
    return make_response("Reviews deleted", HTTPStatus.OK)

@reviews_bp.route('', methods=["POST"])
def create_reviews() -> Response:
    content = request.get_json()
    reviews = Reviews.create_from_dto(content)
    reviews_id = reviews_controller.create(reviews)
    return make_response(f"Reviews with id {reviews_id} created", HTTPStatus.CREATED)

@reviews_bp.route('/bulk', methods=["POST"])
def create_all_reviews() -> Response:
    content = request.get_json()
    reviews = [Reviews.create_from_dto(data) for data in content]
    reviews_controller.create_all(reviews)
    return make_response(reviews_controller.create_all(reviews), HTTPStatus.CREATED)

@reviews_bp.route("/all", methods=["DELETE"])
def delete_all_reviews() -> Response:
    reviews_controller.delete_all()
    return make_response("All Reviews deleted", HTTPStatus.OK)

