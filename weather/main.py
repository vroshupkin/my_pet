import requests
import random
import time

city = {
    "Старый Оскол": 5024
}


def get_page(city_name: str, year: int, month: int):
    url = "https://www.gismfdeo.ru/diary/" + str(city[city_name]) + "/"
    url += str(year) + "/" + str(month) + "/"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'}

    r = requests.get(url, headers=headers)
    return r.text


def save(text: str, save_name: str):
    try:
        f = open(save_name, "x")
    except FileExistsError:
        f = open(save_name, "w")

    f.write(text)
    f.close()


if __name__ == '__main__':
    save_text = get_page("Старый Оскол", 2021, 2)

    save(save_text, "test.html")





