from base_controller import BaseController
from service.property_address_service import PropertyAdressService
class AddressController(BaseController):
    def __init__(self):
        super().__init__(PropertyAdressService())