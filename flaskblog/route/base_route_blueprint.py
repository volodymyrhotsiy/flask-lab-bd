from flask import Blueprint

class BaseRouteBlueprint(Blueprint):
    def __init__(self, name, import_name, route_prefix=None, **kwargs):
        super().__init__(name, import_name, url_prefix=route_prefix, **kwargs)

    def add_route(self, route, methods, controller_func):
        self.route(route, methods=methods)(lambda *args, **kwargs: controller_func(*args, **kwargs))

baser_route_bp = BaseRouteBlueprint()