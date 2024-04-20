from sqlalchemy import text
from app import db
from app.controllers import bp
from flask import render_template


@bp.route('/admin')
def admin_home():
    sql = text("SELECT * FROM cars")
    result = db.session.execute(sql)
    cars = [row for row in result]
    return render_template('admin/index.html', cars=cars)

