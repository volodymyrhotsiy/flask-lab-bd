from flaskblog import db

class BankAccount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_name = db.Column(db.String(45), notnullable=False)
    person_id = db.Column(db.Integer, db.ForeignKey("persone.id"), nullable=False)
    service = db.relationship("Service", backref="reservation", lazy=True)

    def __repr__(self):
        return f"BankAccount('{self.account_name}')"
