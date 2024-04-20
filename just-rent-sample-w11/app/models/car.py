from app import db

class Car(db.Model):
    __tablename__ = 'cars'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    seats = db.Column(db.String(255), nullable=False)
    displacement = db.Column(db.String(255), nullable=False)
    Fuel_tank = db.Column(db.String(255), nullable=False)
    suitcase = db.Column(db.String(255))

