# API source: https://openweathermap.org/
from urllib import response
from os import getenv
import requests

API_KEY = getenv("api_weather_key")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
requests_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(requests_url)

if response.status_code == 200:  # success
    weather_data = response.json()
    weather = weather_data['weather'][0]['description']
    print("Weather:", weather)
    temperature = round(weather_data['main']['temp'] - 273.15, 2)
    print("Temperature:", temperature, "celsius")
else:
    print(f"Error {response.status_code}")
