from base_servise import BaseService
from domain.property_stats import PropertyStats

class PropertyStatsService(BaseService):
    def create_item(self, data):
        return PropertyStats(number_of_bedrooms=data["number_of_bedrooms"], number_of_bathrooms=data["number_of_bathrooms"], max_guests=data["max_guests"], price_per_night=data["price_per_night"])