from flaskblog import db

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