from app import db

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

    wishlists = db.relationship('wishlist', backref='car', lazy=True)

