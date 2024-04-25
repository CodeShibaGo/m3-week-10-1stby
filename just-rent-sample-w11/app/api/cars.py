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
