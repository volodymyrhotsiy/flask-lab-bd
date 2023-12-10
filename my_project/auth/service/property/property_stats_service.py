from my_project.auth.dao import property_stats_dao
from my_project.auth.service.general_service import GeneralService


class PropertyStatsService(GeneralService):
    _dao = property_stats_dao