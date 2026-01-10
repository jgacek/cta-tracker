import os
import sys
import requests

CTA_BUS_API_KEY = os.getenv('CTA_BUS_API_KEY', None)
CTA_BUS_URL = 'https://www.ctabustracker.com/bustime/api/v3/getpredictions'

# route = '56'
# stop_id = '18358'

def get_bus_arrivals(route, stop_id):
    if CTA_BUS_API_KEY is None:
        print("CTA_BUS_API_KEY is not defined")
        sys.exit(1)

    params = {'key': CTA_BUS_API_KEY, 'rt': route, 'stpid': stop_id, 'format': 'json'}

    try:
        response = requests.get(CTA_BUS_URL, params=params)
        response.raise_for_status()
        json = response.json()
        print(json)


    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the request: {e}")


if __name__ == "__main__":
    map_id = int(sys.argv[1])
    stop_id = int(sys.argv[2])
    get_bus_arrivals(map_id, stop_id)
