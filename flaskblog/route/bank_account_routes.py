from base_route_blueprint import BaseRouteBlueprint
from controller.bank_account_controller import (
    add_bank_account_route,
    get_bank_account_route,
    get_bank_account_by_id_route,
    edit_bank_account_route,
    delete_bank_account_route,
)

class BankAccountRouteBlueprint(BaseRouteBlueprint):
    def __init__(self):
        super().__init__("bank_account", __name__)

        self.add_route("/bank_account", ["POST"], add_bank_account_route)
        self.add_route("/bank_account", ["GET"], get_bank_account_route)
        self.add_route("/bank_account/<int:account_id>", ["GET"], get_bank_account_by_id_route)
        self.add_route("/bank_account/<int:account_id>", ["PUT"], edit_bank_account_route)
        self.add_route("/bank_account/<int:account_id>", ["DELETE"], delete_bank_account_route)

bank_account_bp = BankAccountRouteBlueprint()