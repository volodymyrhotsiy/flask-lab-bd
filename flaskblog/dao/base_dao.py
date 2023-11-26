from flaskblog import db

class BaseDAO:
    def add_item(self, item):
        db.session.add(item)
        db.session.commit()
        return {"message": f"{self.model.__name__} added successfully"}

    def get_items(self):
        items = self.model.query.all()
        return [self._serialize(item) for item in items]

    def get_item_by_id(self, item_id):
        item = self.model.query.get(item_id)
        if item:
            return self._serialize(item)
        else:
            raise ValueError(f"{self.model.__name__} with ID {item_id} not found")

    def edit_item(self, item_id, data):
        item = self.model.query.get(item_id)
        self._update_item(item, data)
        db.session.commit()
        return {"message": f"{self.model.__name__} with ID {item_id} updated successfully"}

    def delete_item(self, item_id):
        item = self.model.query.get(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": f"{self.model.__name__} with ID {item_id} deleted successfully"}

    def _serialize(self, item):
        raise NotImplementedError("Subclasses must implement this method")

    def _update_item(self, item, data):
        raise NotImplementedError("Subclasses must implement this method")