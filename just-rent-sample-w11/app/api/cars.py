from flask import jsonify
from app.api import bp

@bp.route('/api/cars', methods=['GET'])
def get_cars(): 
  return jsonify([{'車款': '2024 Toyota Crown 皇家版', '售價': ' 207 ', '排氣量': '2393cc', '車身型式': '轎車,跨界休旅車', '座位數': '5人座', '車門數': '4門', '車長': '4980mm', '軸距': '2850mm', '平均油耗': '15.6km/ltr'}])