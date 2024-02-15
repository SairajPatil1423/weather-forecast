api = "71bac38d686e2468ce1f3ce5ff671ca6"

import  requests


def get_data(place, days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api}"
    response = requests.get(url)
    data = response.json()
    filter_data = data["list"]
    nr_values = 8 * days
    filter_data = filter_data[:nr_values]
    return filter_data
# url = api key from weather forcast web


if __name__ == "__main__":

    print(get_data(place="tokyo"))