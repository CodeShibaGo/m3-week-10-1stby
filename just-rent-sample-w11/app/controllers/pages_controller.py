import datetime
from flask_login import current_user, login_required, login_user, logout_user
from sqlalchemy import text
from app.controllers import bp
from flask import flash, redirect, render_template, request, session, url_for
from app import db
from app.models.booking import Booking, BookingStatus
from app.models.car import CarStatus
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

@bp.route('/booking', methods=['GET', 'POST'])
def booking():
    if request.method == 'POST':
        car_id = request.form['carid']
        pick_up_location_name = request.form['pick_up_location']
        drop_off_location_name = request.form['drop_off_location']
        pick_up_date = request.form['Pick Up Date']
        pick_up_time = request.form['Pick Up Time']
        return_date = request.form['Collection Date']
        return_time = request.form['Collection Time']


        pick_up_datetime = datetime.datetime.strptime(f"{pick_up_date} {pick_up_time}", '%Y-%m-%d %H:%M')
        return_datetime = datetime.datetime.strptime(f"{return_date} {return_time}", '%Y-%m-%d %H:%M')

        car_query = text('SELECT * FROM cars WHERE id = :id AND Status = :Status')
        car_status = db.session.execute(car_query, {'id': car_id, 'Status': CarStatus.AVAILABLE}).fetchone()

        pick_up_location_query = text('SELECT * FROM locations WHERE name = :name')
        pick_up_location = db.session.execute(pick_up_location_query, {'name': pick_up_location_name}).fetchone()

        drop_off_location_query = text('SELECT * FROM locations WHERE name = :name')
        drop_off_location = db.session.execute(drop_off_location_query, {'name': drop_off_location_name}).fetchone()


        current_datetime = datetime.datetime.now()

        if pick_up_datetime < current_datetime:
            return "預訂時間必須晚於當前時間"

        if return_datetime <= pick_up_datetime:
            return "還車時間必須晚於租車時間"

        if car_status and pick_up_location and drop_off_location:
            new_booking = Booking(
                user_id=current_user.id,
                car_id=car_id,
                pick_up_location_id=pick_up_location.id,
                drop_off_location_id=drop_off_location.id,
                pick_up_datetime=pick_up_datetime,
                return_datetime=return_datetime,
                Status=BookingStatus.PENDING
            )
            db.session.add(new_booking)

            car_update = text('UPDATE cars SET Status = :Status WHERE id = :id')
            db.session.execute(car_update, {'Status': CarStatus.BOOKED, 'id': car_id})
            
            db.session.commit()
            return "成功！"
        else:
            return "車輛或地點不可用或不存在"
    else:
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