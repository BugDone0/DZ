import requests

# Ключ уже не работает :Э
API_KEY = "62257f8c7c2a0c5ecb2e87a216dfb71b"

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  
    }

    response = requests.get(BASE_URL, params=params)


    if response.status_code == 200:
        data = response.json()

        temperature = data["main"]["temp"]
        weather_description = data["weather"][0]["description"]

        print(f"Текущая температура в городе {city}: {temperature}°C")
        print(f"Описание погоды: {weather_description.capitalize()}")
    else:
        print(f"Ошибка: Не удалось получить данные. Код статуса: {response.status_code}")


city = input("Введите название города: ")
get_weather(city)
