from flaskblog import db
from datetime import datetime

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Float(), nullable=False)
    comment = db.Column(db.String(45))
    review_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    person_id = db.Column(db.Integer, db.ForeignKey("persone.id"), nullable=False)

    def __repr__(self):
        return f"Review(rating={self.rating}, comment='{self.comment}', review_date={self.review_date})"
