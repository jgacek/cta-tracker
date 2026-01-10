import os
import sys
import requests

WEATHER_API_KEY = os.getenv('WEATHER_API_KEY', None)
WEATHER_URL = 'http://api.weatherapi.com/v1/forecast.json'

def get_weather(location):
    if WEATHER_API_KEY is None:
        print("WEATHER_API_KEY is not defined")
        sys.exit(1)

    params = {'key':WEATHER_API_KEY, 'q': location, 'days': 3, 'aqi': 'no', 'alerts': 'no'}

    try:
        response = requests.get(WEATHER_URL, params=params)
        response.raise_for_status()
        json = response.json()
        print(json)


    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the request: {e}")


if __name__ == "__main__":
    get_weather(sys.argv[1])