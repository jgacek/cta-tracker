import os
import sys
import requests
import xml.etree.ElementTree as ET

cta_train_api_key = os.getenv('CTA_TRAIN_API_KEY', None)
cta_train_url = 'http://lapi.transitchicago.com/api/1.0/ttarrivals.aspx'
map_id = '40380'

if cta_train_api_key is None:
    print("CTA_TRAIN_API_KEY is not defined")
    sys.exit(1)

params = {'key': cta_train_api_key, 'mapid': map_id}

try:
    response = requests.get(cta_train_url, params=params)

    response.raise_for_status()

    xml_data = response.content

    print(xml_data)

    root = ET.fromstring(xml_data)

    print(f"Root tag: {root.tag}")


except requests.exceptions.RequestException as e:
    print(f"An error occurred during the request: {e}")
except ET.ParseError as e:
    print(f"An error occurred during XML parsing: {e}")