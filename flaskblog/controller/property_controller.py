from base_controller import BaseController
from service.property_service import PropertyService

class PropertyController(BaseController):
    def __init__(self):
        super().__init__(PropertyService())