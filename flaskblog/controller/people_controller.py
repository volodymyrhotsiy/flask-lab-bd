from service.people_service import PeopleService
from base_controller import BaseController

class PeopleController(BaseController):
    def __init__(self):
        super().__init__(PeopleService())
