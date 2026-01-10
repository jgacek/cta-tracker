import os
import sys
import requests

weather_api_key = os.getenv('WEATHER_API_KEY', None)
weather_url = 'http://api.weatherapi.com/v1/forecast.json'
location = 'Chicago'

if weather_api_key is None:
    print("WEATHER_API_KEY is not defined")
    sys.exit(1)

params = {'key':weather_api_key, 'q': location, 'days': 3, 'aqi': 'no', 'alerts': 'no'}

try:
    response = requests.get(weather_url, params=params)
    response.raise_for_status()
    json = response.json()
    print(json)


except requests.exceptions.RequestException as e:
    print(f"An error occurred during the request: {e}")