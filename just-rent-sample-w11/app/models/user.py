from flask_login import UserMixin
from app import db
from app.models.wishlist import Wishlist

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    is_admin = db.Column(db.Boolean,default=False)
    
    wishlists = db.relationship('Wishlist', backref='user', lazy=True)



    def get_id(self):
        return str(self.id)