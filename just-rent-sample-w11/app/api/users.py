from flask import jsonify, request, session
from flask_login import login_required
from sqlalchemy import text
from app.api import bp
from app import db


@bp.route('/api/my_wishlist', methods=['POST'])
def add_wishlist():
    data = request.get_json()
    car_id = data['car_id']
    user_id = session.get('user_id')
    print(f"User ID from session: {user_id}")  

    if user_id:
        create = text('INSERT INTO wishlist (user_id, car_id) VALUES (:user_id, :car_id)')
        db.session.execute(create, {'user_id': user_id, 'car_id': car_id})
        db.session.commit()
        return jsonify({'message': 'success'})
    else:
        return jsonify({'message': 'error'}), 401

@bp.route('/api/my_wishlist', methods=['DELETE'])
def remove_wishlist():
    data = request.get_json()
    car_id = data['car_id']
    user_id = session.get('user_id')

    if user_id:
        delete = text('DELETE FROM wishlist WHERE user_id = :user_id AND car_id = :car_id')
        db.session.execute(delete, {'user_id': user_id, 'car_id': car_id})
        db.session.commit()
        return jsonify({'message': 'success'})
    else:
        return jsonify({'message': 'error'}), 401
