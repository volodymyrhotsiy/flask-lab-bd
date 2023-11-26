from base_servise import BaseService
from domain.photo import Photo

class PhotoService(BaseService):
    def create_item(self, data):
        return Photo(photo_url=data["photo_url"], person_id=data["person_id"])
