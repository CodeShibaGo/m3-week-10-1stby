from app import db

class Location(db.Model):
    __tablename__ = 'locations'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    address = db.Column(db.String(256), nullable=False)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)