from flask import jsonify
from app.api import bp
from app import db
from sqlalchemy import text

@bp.route('/api/cars', methods=['GET'])
def get_cars(): 
    query = text('SELECT * FROM cars')
    cars = db.session.execute(query)

    cars_list = [dict(row._mapping) for row in cars]
    return jsonify(cars_list)

@bp.route('/api/cars/<int:id>', methods = ['GET'])
def get_car(id):
    query = text('SELECT * FROM cars WHERE id = :id')
    car = db.session.execute(query, {'id': id}).fetchone()._asdict()
    return jsonify(car)


@bp.route('/api/cars/popular', methods=['GET'])
def get_popular_car():
    query = text('SELECT * FROM cars ORDER BY booking_count DESC LIMIT 5')
    popular_cars = db.session.execute(query)

    popular_car_list = [dict(row._mapping) for row in popular_cars]
    return jsonify(popular_car_list)

