from domain.photo import Photo
from base_dao import BaseDAO

class PhotoDAO(BaseDAO):
    model = Photo

    def _serialize(self, photo):
        return {"id": photo.id, "photo_url": photo.photo_url, "person_id": photo.person_id}

    def _update_item(self, photo, data):
        photo.photo_url = data.get("photo_url", photo.photo_url)
