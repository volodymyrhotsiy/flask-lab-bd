from flask import request, jsonify

class BaseController:
    def __init__(self, service):
        self.service = service

    def add_item(self):
        data = request.get_json()
        result = self.service.add_item(data)
        return jsonify(result)

    def get_items(self):
        items = self.service.get_items()
        return jsonify(items)

    def get_item_by_id(self):
        item_id = request.view_args.get('item_id')
        item = self.service.get_item_by_id(item_id)
        return jsonify(item)

    def edit_item(self):
        item_id = request.view_args.get('item_id')
        data = request.get_json()
        result = self.service.edit_item(item_id, data)
        return jsonify(result)

    def delete_item(self):
        item_id = request.view_args.get('item_id')
        result = self.service.delete_item(item_id)
        return jsonify(result)