from app.controllers import bp
from flask import render_template




@bp.route('/')
def home():
    return render_template('index.html', title='Home')

@bp.route('/cars')
def cars():
    return render_template('cars.html', title='Cars')

@bp.route('/booking')
def booking():
    return render_template('booking.html', title='booking')

@bp.route('/my-account')
def my_account():
    return render_template('account-profile.html')

@bp.route('/login')
def login():
    return render_template('login.html')

@bp.route('/register')
def register():
    return render_template('register.html')