from dao.base_dao import db
from datetime import datetime

class Persone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    photos = db.relationship("Photo", backref="persone", lazy=True)
    reviews = db.relationship("Review", backref="persone", lazy=True)
    account = db.relationship("BankAccount", backref="persone", lazy=True)
    property = db.relationship("Property", backref="persone", lazy=True)
    reservation = db.relationship("Reservation", backref="persone", lazy=True)
    reservation_hitsory = db.relationship(
        "ReservationHistory", backref="persone", lazy=True
    )

    def __repr__(self):
        return f"Persone('{self.first_name}' {self.last_name})"


class Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    photo_url = db.Column(db.String(45))
    person_id = db.Column(db.Integer, db.ForeignKey("persone.id"), nullable=False)

    def __repr__(self):
        return f"(Photo of {self.persone.id} '{self.photo_url}')"


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Float(), nullable=False)
    comment = db.Column(db.String(45))
    review_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    person_id = db.Column(db.Integer, db.ForeignKey("persone.id"), nullable=False)

    def __repr__(self):
        return f"Review(rating={self.rating}, comment='{self.comment}', review_date={self.review_date})"



class BankAccount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_name = db.Column(db.String(45), notnullable=False)
    person_id = db.Column(db.Integer, db.ForeignKey("persone.id"), nullable=False)
    service = db.relationship("Service", backref="reservation", lazy=True)

    def __repr__(self):
        return f"BankAccount('{self.account_name}')"


class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey("persone.id"), nullable=False)
    property_stats_id = db.Column(db.Integer, db.ForeignKey("property_stats.id", nullable=False))
    property_adress_id = db.Column(db.Integer, db.ForeignKey("property_adress.id", nullable=False))

    # Add the many-to-many relationship
    reservations = db.relationship("Reservation", secondary="property_has_reservations", back_populates="properties")

    def __repr__(self):
        return f"Property(person_id={self.person_id}, property_stats={self.property_stats}, property_adress={self.property_adress})"


class PropertyStats(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number_of_bedrooms = db.Column(db.Integer, nullable=False)
    number_of_bathrooms = db.Column(db.Integer, nullable=False)
    max_guests = db.Column(db.Integer, nullable=False)
    price_per_night = db.Column(db.Integer, nullable=False)
    property = db.relationship("Property", backref="property_stats", lazy=True)

    def __repr__(self):
        return f"PropertyStats(number_of_bedrooms={self.number_of_bedrooms}, number_of_bathrooms={self.number_of_bathrooms}, max_guests={self.max_guests}, price_per_night={self.price_per_night})"



class PropertyAdress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.String(30), nullable=False)
    street = db.Column(db.String(30), nullable=False)
    street_number = db.Column(db.String(30), nullable=False)
    property = db.relationship("Property", backref="property_stats", lazy=True)

    def __repr__(self):
        return f"PropertyAdress(state='{self.state}', street='{self.street}', street_number='{self.street_number}')"


class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    total_cost = db.Column(db.Float, nullable=False)  # Corrected the misspelled attribute name
    status = db.Column(db.String(20), nullable=False)
    person_id = db.Column(db.Integer, db.ForeignKey("persone.id"), nullable=False)
    reservation_time_id = db.Column(db.Integer, db.ForeignKey("reservation_time.id", nullable=False))

    # Add the many-to-many relationship
    properties = db.relationship("Property", secondary="property_has_reservations", back_populates="reservations")

    def __repr__(self):
        return f"Reservation(total_cost={self.total_cost}, status='{self.status}', person_id={self.person_id}, reservation_time={self.reservation_time})"


class ReservationTime(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    check_in_date = db.Column(db.DateTime, nullable=False)
    check_out_date = db.Column(db.DateTime, nullable=False)
    reservation = db.relationship("Reservation", backref="reservation_time", lazy=True)

    def __repr__(self):
        return f"ReservationTime(check_in_date={self.check_in_date}, check_out_date={self.check_out_date})"


class ReservationHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reservations = db.relationship(
        "Reservation", backref="reservation_history", lazy=True
    )
    person_id = db.Column(db.Integer, db.ForeignKey("persone.id"), nullable=False)

    def __repr__(self):
        return f"ReservationHistory(person_id={self.person_id})"


class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bank_account_first = db.Column(
        db.Integer, db.ForeignKey("bank_account.id"), nullable=False
    )
    bank_account_second = db.Column(
        db.Integer, db.ForeignKey("bank_account.id"), nullable=False
    )
    reservation_id = db.Column(
        db.Integer, db.ForeignKey("reservation.id"), nullable=False
    )

    def __repr__(self):
        return f"Service(bank_account_first={self.bank_account_first}, bank_account_second={self.bank_account_second}, reservation_id={self.reservation_id})"
    
class PropertyHasReservations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    property_id = db.Column(db.Integer, db.ForeignKey("property.id"), nullable=False)
    reservation_id = db.Column(db.Integer, db.ForeignKey("reservation.id"), nullable=False)

    def __repr__(self):
        return f"PropertyHasReservations(property_id={self.property_id}, reservation_id={self.reservation_id})"