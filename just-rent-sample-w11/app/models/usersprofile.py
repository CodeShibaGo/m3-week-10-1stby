from app import db
class UsersProfile(db.Model):
    __tablename__ = 'user_profile'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    language = db.Column(db.String(255), nullable=False)
    hour_format = db.Column(db.String(255), nullable=False)
