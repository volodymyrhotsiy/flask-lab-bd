from flaskblog import db

class Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    photo_url = db.Column(db.String(45))
    person_id = db.Column(db.Integer, db.ForeignKey("persone.id"), nullable=False)

    def __repr__(self):
        return f"(Photo of {self.persone.id} '{self.photo_url}')"