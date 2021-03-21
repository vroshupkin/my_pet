from bs4 import BeautifulSoup


def read_html(file):
    f = open(file, "r")
    return f.read()


def get_temperature(soup_instance):
    temperature = soup_instance.find_all("td", {"class": "first_in_group"})
    day_temp = []
    night_temp = []

    for i in range(len(temperature)):
        text = str(temperature[i])
        text = text[27:-5]

        if len(text) > 30:
            text = 'None'

        if text[:9] == 'ositive">':
            text = text[9:]

        if i % 2 == 0:
            day_temp.append(text)
        if i % 2 == 1:
            night_temp.append(text)

    # print(day_temp)
    # print(night_temp)


def get_pressure(soup_instance):
    pressure_html = soup_instance.find_all("td")
    day_pressure = []
    night_pressure = []

    for i in range(2, len(pressure_html), 11):
        day_pressure_text = str(pressure_html[i])
        day_pressure_text = day_pressure_text[4:-5]
        if len(day_pressure_text) > 30:
            day_pressure_text = "None"
        day_pressure.append(day_pressure_text)

        night_pressure_text = str(pressure_html[i+5])
        night_pressure_text = night_pressure_text[4:-5]
        if len(night_pressure_text) > 30:
            night_pressure_text = "None"
        night_pressure.append(night_pressure_text)

    print(day_pressure)
    print(night_pressure)


if __name__ == '__main__':
    soup = BeautifulSoup(read_html("test.html"))
    get_temperature(soup)
    get_pressure(soup)

