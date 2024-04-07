from app import db

class Booking (db.Model):
    __tablename__ = 'booking'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    car_id = db.Column(db.Integer, db.ForeignKey('cars.id'), nullable=False)
    pick_up_location_id = db.Column(db.Integer, db.ForeignKey('locations.id'), nullable=False)
    drop_off_location_id = db.Column(db.Integer, db.ForeignKey('locations.id'), nullable=False)
    pick_up_time = db.Column(db.DateTime, nullable=False)
    return_time = db.Column(db.DateTime, nullable=False)

    user = db.relationship('User', backref='bookings')
    car = db.relationship('Car', backref='bookings')    