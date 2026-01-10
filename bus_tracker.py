import os
import sys
import requests
from datetime import datetime

CTA_BUS_API_KEY = os.getenv('CTA_BUS_API_KEY', None)
CTA_BUS_URL = 'https://www.ctabustracker.com/bustime/api/v3/getpredictions'
CTA_BUS_TIME_FORMAT = '%Y%m%d %H:%M'


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
        for bus in json.get('bustime-response').get('prd'):
            print_bus_arrival(bus, route)


    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the request: {e}")


def print_bus_arrival(bus, route):
    direction = bus.get('rtdir')
    stop_name = bus.get('stpnm')
    minutes_til_arrival = calculate_minutes_til_arrival(bus.get('prdtm'))
    print(f"{route} {direction} arriving at {stop_name} in {minutes_til_arrival} minutes(s)")


def calculate_minutes_til_arrival(arrival_time):
    current_time = datetime.now()
    formatted_arrival_time = datetime.strptime(arrival_time, CTA_BUS_TIME_FORMAT)
    delta = formatted_arrival_time - current_time
    return int(delta.total_seconds() / 60)


if __name__ == "__main__":
    r = int(sys.argv[1])
    stpid = int(sys.argv[2])
    get_bus_arrivals(r, stpid)
