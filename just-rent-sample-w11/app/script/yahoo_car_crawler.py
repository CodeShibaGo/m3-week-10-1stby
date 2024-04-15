from selenium import webdriver
from selenium.webdriver.edge.options import Options
import time
from bs4 import BeautifulSoup
import  json

def yahoo_car_crawler(url):
    options = Options()
    options.headless = True
    driver = webdriver.Edge(options=options)

    driver.get(url)
    time.sleep(3)

    # final_url = driver.current_url
    # print(final_url)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    spec_wrapper = soup.find('div', {'class': 'spec-wrapper'})
    if spec_wrapper is None:
        return None
    fields_dict = {
        'displacement': '排氣量',
        'body': '車身型式',
        'seat': '座位數',
        'brand': '廠牌',
        'model': '車款',
    }



    # 找到標題
    info_dict = {}
    title = soup.find('title').text
    car_name = title.split('|')[0].strip()
    print(car_name)
    info_dict['name'] = car_name

    for field_key, field in fields_dict.items():
        field_info = spec_wrapper.find('span', text=field)
        if field_info is not None:
            field_value = field_info.find_next_sibling('span').text
            info_dict[field_key] = field_value
        else:
            info_dict[field_key] = None

    driver.quit()
    print(info_dict)
    return info_dict

#從car_list.json爬取好的起車資料讀進來
with open("car_list.json", "r") as file:
    car_list = json.load(file)

cars_info = []
count = 0
for car in car_list:
    short_link = car['short_link']
    if short_link is not None:
        url = short_link
        car_info = yahoo_car_crawler(url)
        if car_info is not None:
            cars_info.append(car_info)
            count += 1
            if count == 3:
                break
print(cars_info)

with open("cars.json", "w") as file:
    json.dump(cars_info, file)