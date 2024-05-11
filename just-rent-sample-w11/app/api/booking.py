import datetime
from flask import jsonify, request
from flask_login import current_user
from sqlalchemy import text
from app.api import bp
from app import db
from app.models.booking import Booking, BookingStatus
from app.models.car import CarStatus

@bp.route('/api/booking', methods=['POST'])
def add_booking():

    car_id = request.form['carId']
    pick_up_location_name = request.form['pickUpLocation']
    drop_off_location_name = request.form['dropOffLocation']
    pick_up_date = request.form['PickUpDate']
    pick_up_time = request.form['PickUpTime']
    return_date = request.form['returnDate']
    return_time = request.form['returnTime']

    pick_up_datetime = datetime.datetime.strptime(f"{pick_up_date} {pick_up_time}", '%Y-%m-%d %H:%M')
    return_datetime = datetime.datetime.strptime(f"{return_date} {return_time}", '%Y-%m-%d %H:%M')

    car_query = text('SELECT * FROM cars WHERE id = :id AND Status = :Status')
    car_status = db.session.execute(car_query, {'id': car_id, 'Status': CarStatus.AVAILABLE}).fetchone()

    location_query = text('SELECT * FROM locations WHERE name = :name')
    pick_up_location = db.session.execute(location_query, {'name': pick_up_location_name}).fetchone()
    drop_off_location = db.session.execute(location_query, {'name': drop_off_location_name}).fetchone()

    current_datetime = datetime.datetime.now()

    if pick_up_datetime < current_datetime:
        return jsonify({'message': '預訂時間必須晚於當前時間'})

    if return_datetime <= pick_up_datetime:
        return jsonify({'message': '還車時間必須晚於租車時間'})

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
        return jsonify({'message': 'success'})
    else:
        return jsonify({'message':'租車失敗'})


