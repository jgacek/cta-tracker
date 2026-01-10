import os
import sys
import requests

WEATHER_API_KEY = os.getenv('WEATHER_API_KEY', None)
WEATHER_URL = 'http://api.weatherapi.com/v1/forecast.json'


def get_weather(location):
    if WEATHER_API_KEY is None:
        print("WEATHER_API_KEY is not defined")
        sys.exit(1)

    params = {'key': WEATHER_API_KEY, 'q': location, 'days': 1, 'aqi': 'no', 'alerts': 'no'}

    try:
        response = requests.get(WEATHER_URL, params=params)
        response.raise_for_status()
        json = response.json()
        current_weather = json.get('current')
        today_forecast = json.get('forecast').get('forecastday')[0].get('day')
        print_current_forecast(current_weather)
        print_today_forecast(today_forecast)

    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the request: {e}")


def print_current_forecast(current):
    temp_f = current.get('temp_f')
    feels_like_f = current.get('feelslike_f')
    temp_c = current.get('temp_c')
    feels_like_c = current.get('feelslike_c')
    condition = current.get('condition').get('text')
    print(f"{temp_f}F ({temp_c}C)\nFeels like {feels_like_f}F ({feels_like_c}C)\n{condition}")


def print_today_forecast(today):
    max_temp_f = today.get('maxtemp_f')
    min_temp_f = today.get('mintemp_f')
    max_temp_c = today.get('maxtemp_c')
    min_temp_c = today.get('mintemp_c')
    print(f"Today's high: {max_temp_f}F ({max_temp_c}C)\nToday's low: {min_temp_f}F ({min_temp_c}C)")


if __name__ == "__main__":
    get_weather(sys.argv[1])
