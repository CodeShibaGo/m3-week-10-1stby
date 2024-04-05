import requests
from bs4 import BeautifulSoup
def yahoo_car_crawler():
    url = "https://autos.yahoo.com.tw/new-cars/trim/toyota-crown-2024-%E7%9A%87%E5%AE%B6%E7%89%88/spec#car-trim-nav"  # 將網址存入變數
    response = requests.get(url)  # 發送 GET 請求
    soup = BeautifulSoup(response.text, "html.parser")  # 解析 HTML

    # 使用 CSS 選擇器來選取元素
    car_info = {
        "車款": soup.select_one(".trim-main h1.title").text,
        "售價": soup.select_one(".trim-main h3.price font").text,
        "排氣量": soup.select_one(".spec-wrapper ul li:nth-child(3) span:nth-child(2)").text,
        "車身型式": soup.select_one(".spec-wrapper  ul:nth-of-type(4) li span:nth-child(2)").text,
        "座位數": soup.select_one(".spec-wrapper ul:nth-of-type(4) li:nth-child(3) span:nth-child(2)").text,
        "車門數": soup.select_one(".spec-wrapper ul:nth-of-type(4) li:nth-child(2) span:nth-child(2)").text,
        "車長": soup.select_one(".spec-wrapper ul:nth-of-type(4) li:nth-child(4) span:nth-child(2)").text,
        "軸距": soup.select_one(".spec-wrapper ul:nth-of-type(4) li:nth-child(8) span:nth-child(2)").text,
        "平均油耗": soup.select_one(".spec-wrapper ul:nth-of-type(5) li:nth-child(4) span:nth-child(2)").text
    }

    print(car_info)
yahoo_car_crawler()
