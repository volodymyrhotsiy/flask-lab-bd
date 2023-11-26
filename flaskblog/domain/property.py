from flaskblog import db

class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey("persone.id"), nullable=False)
    property_stats = db.Column(
        db.Integer, db.ForeignKey("property_stats.id", nullable=False)
    )
    property_adress = db.Column(
        db.Integer, db.ForeignKey("property_adress.id", nullable=False)
    )

    def __repr__(self):
        return f"Property(person_id={self.person_id}, property_stats={self.property_stats}, property_adress={self.property_adress})"
