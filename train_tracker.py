import os
import sys
import requests
from datetime import datetime

CTA_TRAIN_API_KEY = os.getenv('CTA_TRAIN_API_KEY', None)
CTA_TRAIN_URL = 'http://lapi.transitchicago.com/api/1.0/ttarrivals.aspx'
CTA_TRAIN_TIME_FORMAT = '%Y-%m-%dT%H:%M:%S'


# Map id for Western/Milwaukee blue line stop. Can reference full list here https://www.transitchicago.com/developers/ttdocs/#_Toc296199909
# map_id = '40670'

def get_train_arrivals(map_id):
    if CTA_TRAIN_API_KEY is None:
        print("CTA_TRAIN_API_KEY is not defined")
        sys.exit(1)

    params = {'key': CTA_TRAIN_API_KEY, 'mapid': map_id, 'max': 5, 'outputType': 'json'}

    try:
        response = requests.get(CTA_TRAIN_URL, params=params)
        response.raise_for_status()
        json = response.json()
        print(json)
        for train in json.get('ctatt').get('eta'):
            print_train_arrival(train)



    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the request: {e}")


def print_train_arrival(train):
    station = train.get('staNm')
    final_destination = train.get('destNm')
    route = train.get('rt')
    minutes_til_arrival = calculate_minutes_til_arrival(train.get('arrT'))
    print(f"{route} Line with service towards {final_destination} arriving at {station} in {minutes_til_arrival} minute(s)")


def calculate_minutes_til_arrival(arrival_time):
    current_time = datetime.now()
    formatted_arrival_time = datetime.strptime(arrival_time, CTA_TRAIN_TIME_FORMAT)
    delta = formatted_arrival_time - current_time
    return int(delta.total_seconds() / 60)


if __name__ == "__main__":
    get_train_arrivals(sys.argv[1])
