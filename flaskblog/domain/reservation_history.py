from flaskblog import db

class ReservationHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reservations = db.relationship(
        "Reservation", backref="reservation_history", lazy=True
    )
    person_id = db.Column(db.Integer, db.ForeignKey("persone.id"), nullable=False)

    def __repr__(self):
        return f"ReservationHistory(person_id={self.person_id})"
