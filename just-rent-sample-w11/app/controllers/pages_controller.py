from app.controllers import bp
from flask import render_template




@bp.route('/')
def home():
    return render_template('index.html', title='Home')

@bp.route('/cars')
def cars():
    return render_template('cars.html', title='Cars')

@bp.route('/cars-list')
def cars_list():
    return render_template('cars-list.html')

@bp.route('/car-single')
def car_single():
    return render_template('car-single.html')

@bp.route('/booking')
def booking():
    return render_template('booking.html', title='booking')

@bp.route('/my-profile')
def account_profile():
    return render_template('account-profile.html')

@bp.route('/my-orders')
def account_booking():
    return render_template('account-booking.html')

@bp.route('/my-favorite-car')
def account_favorite():
    return render_template('account-favorite.html')

@bp.route('/login')
def login():
    return render_template('login.html')

@bp.route('/register')
def register():
    return render_template('register.html')