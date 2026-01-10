import os
import sys
import requests

CTA_TRAIN_API_KEY = os.getenv('CTA_TRAIN_API_KEY', None)
CTA_TRAIN_URL = 'http://lapi.transitchicago.com/api/1.0/ttarrivals.aspx'
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


    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the request: {e}")


if __name__ == "__main__":
    get_train_arrivals(sys.argv[1])