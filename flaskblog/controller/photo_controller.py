from base_controller import BaseController
from service.photo_service import PhotoService

class PhotoController(BaseController):
    def __init__(self):
        super().__init__(PhotoService())