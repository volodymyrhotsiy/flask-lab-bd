from flask import Flask

def register_routes(app: Flask) -> None:
    from .people.bank_account_route import bank_account_bp
    from .people.people_route import people_bp
    from .people.people_photos_route import people_photos_bp
    from .people.reviews_route import reviews_bp
    from .property.address_route import address_bp
    from .property.property_route import property_bp
    from .property.property_has_reservations_route import property_has_reservations_bp
    from .property.property_stats_route import property_stats_bp
    from .reservation.reservation_route import reservation_bp
    from .reservation.reservation_history_route import reservation_history_bp
    from .reservation.reservation_time_route import reservation_time_bp

    app.register_blueprint(bank_account_bp)
    app.register_blueprint(people_bp)
    app.register_blueprint(people_photos_bp)
    app.register_blueprint(reviews_bp)
    app.register_blueprint(address_bp)
    app.register_blueprint(property_bp)
    app.register_blueprint(property_has_reservations_bp)
    app.register_blueprint(property_stats_bp)
    app.register_blueprint(reservation_bp)
    app.register_blueprint(reservation_history_bp)
    app.register_blueprint(reservation_time_bp)