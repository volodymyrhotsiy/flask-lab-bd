from flaskblog import db

class PropertyAdress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.String(30), nullable=False)
    street = db.Column(db.String(30), nullable=False)
    street_number = db.Column(db.String(30), nullable=False)
    property = db.relationship("Property", backref="property_stats", lazy=True)

    def __repr__(self):
        return f"PropertyAdress(state='{self.state}', street='{self.street}', street_number='{self.street_number}')"
