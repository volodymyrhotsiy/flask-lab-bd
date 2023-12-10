from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import property_stats_service


class PropertyStatsController(GeneralController):
    _service = property_stats_service