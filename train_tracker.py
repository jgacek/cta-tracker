import os
import sys
import requests

cta_train_api_key = os.getenv('CTA_TRAIN_API_KEY', None)
cta_train_url = 'http://lapi.transitchicago.com/api/1.0/ttarrivals.aspx'
# Map id for Western/Milwaukee blue line stop. Can reference full list here https://www.transitchicago.com/developers/ttdocs/#_Toc296199909
map_id = '40670'

if cta_train_api_key is None:
    print("CTA_TRAIN_API_KEY is not defined")
    sys.exit(1)

params = {'key': cta_train_api_key, 'mapid': map_id, 'max': 5, 'outputType': 'json'}

try:
    response = requests.get(cta_train_url, params=params)
    response.raise_for_status()
    json = response.json()
    print(json)


except requests.exceptions.RequestException as e:
    print(f"An error occurred during the request: {e}")