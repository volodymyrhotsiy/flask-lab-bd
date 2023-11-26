from flaskblog import db

class PropertyStats(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number_of_bedrooms = db.Column(db.Integer, nullable=False)
    number_of_bathrooms = db.Column(db.Integer, nullable=False)
    max_guests = db.Column(db.Integer, nullable=False)
    price_per_night = db.Column(db.Integer, nullable=False)
    property = db.relationship("Property", backref="property_stats", lazy=True)

    def __repr__(self):
        return f"PropertyStats(number_of_bedrooms={self.number_of_bedrooms}, number_of_bathrooms={self.number_of_bathrooms}, max_guests={self.max_guests}, price_per_night={self.price_per_night})"
