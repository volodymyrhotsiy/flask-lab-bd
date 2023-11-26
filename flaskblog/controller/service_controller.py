from base_controller import BaseController
from service.service_service import ServiceService

class ServiceController(BaseController):
    def __init__(self):
        super().__init__(ServiceService())