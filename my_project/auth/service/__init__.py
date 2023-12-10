from my_project.auth.service.people.bank_account_service import BankAccountService
from my_project.auth.service.people.people_service import PeopleService
from my_project.auth.service.people.people_photos_service import PeoplePhotosService
from my_project.auth.service.people.reviews_service import ReviewsService
from my_project.auth.service.property.address_service import AddressService
from my_project.auth.service.property.property_service import PropertyService
from my_project.auth.service.property.property_has_reservations_service import PropertyHasReservationsService
from my_project.auth.service.property.property_stats_service import PropertyStatsService
from my_project.auth.service.reservation.reservation_service import ReservationService
from my_project.auth.service.reservation.reservation_history_service import ReservationHistoryService
from my_project.auth.service.reservation.reservation_time_service import ReservationTimeService

bank_account_service = BankAccountService()
people_service = PeopleService()
people_photos_service = PeoplePhotosService()
reviews_service = ReviewsService()
address_service = AddressService()
property_service = PropertyService()
property_has_reservations_service = PropertyHasReservationsService()
property_stats_service = PropertyStatsService()
reservation_service = ReservationService()
reservation_history_service = ReservationHistoryService()
reservation_time_service = ReservationTimeService()