import requests
from bs4 import BeautifulSoup
import  json

def sscar_crawler(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    products = soup.find_all('div', class_='product-small')
    result = []
    for product in products:
        name = product.find('a', class_='woocommerce-LoopProduct-link').text
        url = product.find('a', class_='woocommerce-LoopProduct-link')['href']
        result.append({'name': name, 'url': url})
    return result

def get_yahoo_link(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        link = soup.find_all('h4')[1].find('a')['href']
        return link
    except Exception as e:
        print(f'an error occurred: {e}')
        return None


# 使用範例
url = "https://sscars.com.tw/car/"
cars_list = sscar_crawler(url)
print(cars_list)
for car in cars_list:
    url = car['url']
    if url is not None:
        car['short_link'] = get_yahoo_link(url)
print(car)


# 轉為json格式
cars_list_json = json.dumps(cars_list)

#將轉好的json寫入檔案
with open("car_list.json", "w") as file:
    file.write(cars_list_json)


