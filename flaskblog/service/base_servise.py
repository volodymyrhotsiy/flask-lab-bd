class BaseService:
    def __init__(self, dao):
        self.dao = dao

    def add_item(self, data):
        item = self.create_item(data)
        return self.dao.add_item(item)

    def get_items(self):
        return self.dao.get_items()

    def get_item_by_id(self, item_id):
        return self.dao.get_item_by_id(item_id)

    def edit_item(self, item_id, data):
        return self.dao.edit_item(item_id, data)

    def delete_item(self, item_id):
        return self.dao.delete_item(item_id)

    def create_item(self, data):
        raise NotImplementedError("Subclasses must implement create_item method.")        