from flaskblog import db

class ReservationTime(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    check_in_date = db.Column(db.DateTime, nullable=False)
    check_out_date = db.Column(db.DateTime, nullable=False)
    reservation = db.relationship("Reservation", backref="reservation_time", lazy=True)

    def __repr__(self):
        return f"ReservationTime(check_in_date={self.check_in_date}, check_out_date={self.check_out_date})"
