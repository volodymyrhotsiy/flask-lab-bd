from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify
from my_project.auth.controller import bank_account_controller
from my_project.auth.domain.people.bank_account import BankAccount

bank_account_bp = Blueprint("bank_account", __name__, url_prefix="/bank_account/")
    
@bank_account_bp.route("", methods=["GET"])
def get_all_bank_account() -> Response:
    return make_response(jsonify(bank_account_controller.find_all()), HTTPStatus.OK)

@bank_account_bp.route('/<int:bank_account_id>',  methods=["GET"])
def get_bank_account(bank_account_id: int) -> Response:
    return make_response(jsonify(bank_account_controller.find_by_id(bank_account_id)), HTTPStatus.OK)

@bank_account_bp.route('/<int:bank_account_id>',  methods=["PUT"])
def update_bank_account(bank_account_id: int) -> Response:
    content = request.get_json()
    bank_account = BankAccount.create_from_dto(content)
    bank_account_controller.update(bank_account_id, bank_account)
    return make_response("BankAccount Updated", HTTPStatus.OK)

@bank_account_bp.route('/<int:bank_account_id>',  methods=["PATCH"])
def patch_bank_account(bank_account_id: int) -> Response:
    content = request.get_json()
    bank_account_controller.patch(bank_account_id, content)
    return make_response("BankAccount Updated", HTTPStatus.OK)

@bank_account_bp.route('/<int:bank_account_id>',  methods=["DELETE"])
def delete_bank_account(bank_account_id: int) -> Response:
    bank_account_controller.delete(bank_account_id)
    return make_response("BankAccount deleted", HTTPStatus.OK)

@bank_account_bp.route('',  methods=["POST"])
def create_bank_account() -> Response:
    content = request.get_json()
    bank_account = BankAccount.create_from_dto(content)
    bank_account_id = bank_account_controller.create(bank_account)
    return make_response(f"BankAccount with id {bank_account_id} created", HTTPStatus.CREATED)

@bank_account_bp.route('/bulk',  methods=["POST"])
def create_all_bank_account() -> Response:
    content = request.get_json()
    bank_account = [BankAccount.create_from_dto(data) for data in content]
    bank_account_controller.create_all(bank_account)
    return make_response(bank_account_controller.create_all(bank_account), HTTPStatus.CREATED)

@bank_account_bp.route("/all", methods=["DELETE"])
def delete_all_bank_account() -> Response:
    bank_account_controller.delete_all()
    return make_response("All BankAccount deleted", HTTPStatus.OK)

