from flask_login import login_required, login_user, logout_user
from sqlalchemy import text
from app import db
from app.controllers import bp
from flask import render_template, request, redirect, url_for, flash

from app.models.user import User


@bp.route('/admin')
@login_required
def admin_home():
    sql = text("SELECT * FROM cars")
    result = db.session.execute(sql)
    cars = [row for row in result]
    return render_template('admin/index.html', cars=cars)

@bp.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        sql = text('SELECT * FROM users WHERE username = :username')
        result = db.session.execute(sql, {'username': username}).fetchone()

        if result and result.password == password:
            user = User(id=result.id, username=result.username, password=result.password)
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('controller.admin_home'))
        else:
            flash('無效的用戶名或密碼')
    return render_template('admin/login.html')

@bp.route('/admin/logout')
@login_required
def admin_logout():
    logout_user()
    return redirect(url_for('controller.admin_login'))

@bp.route('/admin/edit_car/<int:car_id>', methods=['GET', 'POST'])
def admin_edit_car(car_id):
    if request.method == 'POST':
        db.session.execute(text("""
            UPDATE cars SET
            name = :name,
            displacement = :displacement,
            body = :body,
            door = :door,
            seats = :seats,
            width = :width,
            height = :height,
            Fuel_tank = :Fuel_tank,
            suitcase = :suitcase
            WHERE id = :car_id
        """), {
            'name': request.form['car_name'],
            'displacement': request.form['car_displacement'],
            'body': request.form['car_body'],
            'door': request.form['car_door'],
            'seats': request.form['car_seats'],
            'width': request.form['car_width'],
            'height': request.form['car_height'],
            'Fuel_tank': request.form['car_Fuel_tank'],
            'suitcase': request.form['car_suitcase'],
            'car_id': car_id
        })

        db.session.commit()
        return redirect(url_for('controller.admin_home'))

    sql = text('SELECT * FROM cars WHERE id = :car_id')
    result = db.session.execute(sql, {'car_id': car_id})
    car = result.fetchone()

    return render_template('admin/edit_car.html', car=car)

@bp.route('/admin/view_car/<int:car_id>')
def admin_view_car(car_id):
    sql = text('SELECT * FROM cars WHERE id = :car_id')
    result = db.session.execute(sql, {'car_id': car_id})
    car = result.fetchone()

    return render_template('admin/view_car.html', car=car)
