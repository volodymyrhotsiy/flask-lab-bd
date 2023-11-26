from flaskblog import db

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bank_account_first = db.Column(
        db.Integer, db.ForeignKey("bank_account.id"), nullable=False
    )
    bank_account_second = db.Column(
        db.Integer, db.ForeignKey("bank_account.id"), nullable=False
    )
    reservation_id = db.Column(
        db.Integer, db.ForeignKey("reservation.id"), nullable=False
    )

    def __repr__(self):
        return f"Service(bank_account_first={self.bank_account_first}, bank_account_second={self.bank_account_second}, reservation_id={self.reservation_id})"
    