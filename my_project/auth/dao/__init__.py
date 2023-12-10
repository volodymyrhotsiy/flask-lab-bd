from .people.bank_account_dao import BankAccountDao
from .people.people_dao import PeopleDao
from .people.people_photos_dao import PeoplePhotosDao
from .people.reviews_dao import ReviewsDao
from .property.address_dao import AddressDao
from .property.property_dao import PropertyDao
from .property.property_has_reservations_dao import PropertyHasReservationsDao
from .property.property_stats_dao import PropertyStatsDao
from .reservation.reservation_dao import ReservationDao
from .reservation.reservation_history_dao import ReservationHistoryDao
from .reservation.reservation_time_dao import ReservationTimeDao

bank_account_dao = BankAccountDao()
people_dao = PeopleDao()
people_photos_dao = PeoplePhotosDao()
reviews_dao = ReviewsDao()
address_dao = AddressDao()
property_dao = PropertyDao()
property_has_reservations_dao = PropertyHasReservationsDao()
property_stats_dao = PropertyStatsDao()
reservation_dao = ReservationDao()
reservation_history_dao = ReservationHistoryDao()
reservation_time_dao = ReservationTimeDao()