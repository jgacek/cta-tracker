import os
import sys
import requests

cta_bus_api_key = os.getenv('CTA_BUS_API_KEY', None)
cta_bus_url = 'https://www.ctabustracker.com/bustime/api/v3/getpredictions'
route = '56'
stop_id = '18358'

if cta_bus_api_key is None:
    print("CTA_BUS_API_KEY is not defined")
    sys.exit(1)

params = {'key': cta_bus_api_key, 'rt': route, 'stpid': stop_id, 'format': 'json'}

try:
    response = requests.get(cta_bus_url, params=params)
    response.raise_for_status()
    json = response.json()
    print(json)


except requests.exceptions.RequestException as e:
    print(f"An error occurred during the request: {e}")