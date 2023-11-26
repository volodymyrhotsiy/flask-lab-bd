from flaskblog import db

class PropertyHasReservations(db.Model):
    property_id = db.relationship(db.Integer, db.ForeignKey("property.id"), nullable=False)
    reservation_id = db.Column(db.Integer, db.ForeignKey("reservation.id"), nullable=False)