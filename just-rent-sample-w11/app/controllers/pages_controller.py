from flask_login import current_user, login_required, login_user, logout_user
from sqlalchemy import text
from app.controllers import bp
from flask import flash, redirect, render_template, request, session, url_for
from app import db
from app.models.user import User
from werkzeug.security import generate_password_hash, check_password_hash



@bp.route('/')
def home():
    
    return render_template('index.html')


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
@login_required
def account_favorite():
    return render_template('account-favorite.html')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('controller.home'))

    if request.method == 'POST':
        username = request.form['name']
        password = request.form['password']
        query = text("SELECT * FROM users WHERE username = :username")
        user = db.session.execute(query, {'username': username}).fetchone()

        if user and check_password_hash(user.password, password): 
            user = User(id=user.id, username=user.username, password=user.password)
            login_user(user) 
            session['user_id'] = user.id
            return redirect(url_for('controller.home'))
        else:
            flash('使用者帳號/密碼錯誤','error')
    return render_template('login.html')

@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('controller.home'))

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['name']
        email = request.form['email']
        password = request.form['password']
        re_password = request.form['re-password']

        if not username or not email or not password or not re_password:
            flash('Please fill in all fields.', 'error')
        elif password != re_password:
            flash('Passwords do not match.', 'error')
        else:
            hashed_password = generate_password_hash(password)
            new_user = User(username=username, email=email, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            flash('註冊成功','success')
            return redirect(url_for('controller.login'))

    return render_template('register.html')