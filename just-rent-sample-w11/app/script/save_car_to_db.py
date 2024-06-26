import json

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import Config
from app.models import Car
#建立資料庫連線
engine = create_engine(Config.SQLALCHEMY_DATABASE_URI, echo=True)
#建立session類別
Session = sessionmaker(bind=engine)
#建立session物件
session = Session()

# 讀取json資料
with open("cars.json", 'r') as file:
    data = json.load(file)
print(data)

for item in data:
    car = Car(
        name=item['name'],
        seats=item['seat']
    )
    session.add(car)
session.commit()
session.close()