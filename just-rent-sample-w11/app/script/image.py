import json
import os.path
import shutil
import requests
from selenium import webdriver
from selenium.webdriver.edge.options import Options
import time
from bs4 import BeautifulSoup

def save_image(url, car_name):
    options = Options()
    driver = webdriver.Edge(options=options)

    driver.get(url)
    time.sleep(3)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    image_tags = soup.find_all('img', {'class': 'gabtn'})

    directory = car_name
    if not os.path.exists(directory):
        os.makedirs(directory)

    for i, img in enumerate(image_tags):
       if i >= 3:
           break
       img_src = img['src']
       response = requests.get(img_src, stream=True)

       if response.status_code == 200:
            response.raw.decode_content = True

            with open(directory + '/img_' + str(i) + '.jpg', 'wb') as f:
                shutil.copyfileobj(response.raw, f)

    driver.quit()

with open("car_list.json", "r") as file:
    car_list = json.load(file)

for car in car_list:
    short_link = car['short_link']
    if short_link is not None:
        url = short_link
        save_image(url, car['name'])
    else:
        print(f"Skipping {car['name']} because short_link is None")