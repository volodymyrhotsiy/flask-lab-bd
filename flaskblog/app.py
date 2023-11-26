from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from route.bank_account_routes import bank_account_bp
from route.address_routes import address_bp
from route.people_routes import people_bp
from route.photo_routes import photo_bp
from route.property_routes import property_bp
from route.base_route_blueprint import baser_route_bp
from route.property_stats_routes import property_stats_bp
from route.reservation_history_routes import reservation_history_bp
from route.reservation_routes import reservation_bp
from route.service_routes import service_bp


app.register_blueprint(baser_route_bp)
app.register_blueprint(bank_account_bp)
app.register_blueprint(address_bp)
app.register_blueprint(people_bp)
app.register_blueprint(photo_bp)
app.register_blueprint(property_bp)
app.register_blueprint(property_stats_bp)
app.register_blueprint(reservation_history_bp)
app.register_blueprint(reservation_bp)
app.register_blueprint(service_bp)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
