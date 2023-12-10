from my_project.auth.dao.gereral_dao import GeneralDAO
from my_project.auth.domain.property.property_stats import PropertyStats


class PropertyStatsDao(GeneralDAO):
    _domain_type = PropertyStats