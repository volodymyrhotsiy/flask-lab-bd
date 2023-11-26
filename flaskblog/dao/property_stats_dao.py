from domain.property_stats import PropertyStats
from base_dao import BaseDAO

class PropertyStatsDAO(BaseDAO):
    model = PropertyStats

    def _serialize(self, property_stats):
        return {
            "id": property_stats.id,
            "number_of_bedrooms": property_stats.number_of_bedrooms,
            "number_of_bathrooms": property_stats.number_of_bathrooms,
            "max_guests": property_stats.max_guests,
            "price_per_night": property_stats.price_per_night
        }

    def _update_item(self, property_stats, data):
        property_stats.number_of_bedrooms = data.get("number_of_bedrooms", property_stats.number_of_bedrooms)
        property_stats.number_of_bathrooms = data.get("number_of_bathrooms", property_stats.number_of_bathrooms)
        property_stats.max_guests = data.get("max_guests", property_stats.max_guests)
        property_stats.price_per_night = data.get("price_per_night", property_stats.price_per_night)
