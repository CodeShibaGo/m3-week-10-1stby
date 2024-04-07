from app import db

class Car(db.Model):
    __tablename__ = 'cars'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    seats = db.Column(db.Integer, nullable=False)
    door_count = db.Column(db.Integer, nullable=False)
    fuel_price = db.Column(db.Float, nullable=False)