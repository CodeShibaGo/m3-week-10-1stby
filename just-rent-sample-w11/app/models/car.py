from app import db
from app.models.wishlist import Wishlist

class CarStatus:
    AVAILABLE = 1 #可租
    BOOKED = 2 #預定中
    RENTED = 3 #以出租

class Car(db.Model):
    __tablename__ = 'cars'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    body = db.Column(db.String(255), nullable=False)
    door = db.Column(db.String(255), nullable=False)
    seats = db.Column(db.String(255), nullable=False)
    width = db.Column(db.String(255), nullable=False)
    height = db.Column(db.String(255), nullable=False)
    displacement = db.Column(db.String(255), nullable=False)
    Fuel_tank = db.Column(db.String(255), nullable=False)
    suitcase = db.Column(db.String(255))
    booking_count = db.Column(db.Integer)
    Status = db.Column(db.Integer, nullable=False)

    wishlists = db.relationship('Wishlist', backref='car', lazy=True)

