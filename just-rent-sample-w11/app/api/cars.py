from flask import jsonify
from app.api import bp
from app import db
from sqlalchemy import text

@bp.route('/api/cars', methods=['GET'])
def get_cars(): 
    sql = text('SELECT * FROM cars')
    result = db.session.execute(sql)

    cars_list = [dict(row._mapping) for row in result]
    return jsonify(cars_list)