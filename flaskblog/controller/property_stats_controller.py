from base_controller import BaseController
from service.property_stats_service import PropertyStatsService

class PropertyStatsController(BaseController):
    def __init__(self):
        super().__init__(PropertyStatsService())