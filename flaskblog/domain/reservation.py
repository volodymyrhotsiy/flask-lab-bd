from flaskblog import db 

class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    totatl_cost = db.Column(db.Double, nullable=False)
    status = db.Column(db.String(20), nullable=False)
    person_id = db.Column(db.Integer, db.ForeignKey("persone.id"), nullable=False)
    reservation_time = db.Column(
        db.Integer, db.ForeignKey("reservation_time.id", nullable=False)
    )
    service = db.relationship("Service", backref="reservation", lazy=True)

    def __repr__(self):
        return f"Reservation(total_cost={self.totatl_cost}, status='{self.status}', person_id={self.person_id}, reservation_time={self.reservation_time})"