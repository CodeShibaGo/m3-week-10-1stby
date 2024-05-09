from app import db

class BookingStatus:
    PENDING = 1 #等待付款
    CONFIRMED = 2 #以確認
    CANCELED = 3 #以取消
    COMPLETED = 4 #完成訂單


class Booking (db.Model):
    __tablename__ = 'booking'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    car_id = db.Column(db.Integer, db.ForeignKey('cars.id'), nullable=False)
    pick_up_location_id = db.Column(db.Integer, db.ForeignKey('locations.id'), nullable=False)
    drop_off_location_id = db.Column(db.Integer, db.ForeignKey('locations.id'), nullable=False)
    pick_up_datetime = db.Column(db.DateTime, nullable=False)
    return_datetime = db.Column(db.DateTime, nullable=False)
    Status = db.Column(db.Integer, nullable=False)


    user = db.relationship('User', backref='bookings')
    car = db.relationship('Car', backref='bookings')    