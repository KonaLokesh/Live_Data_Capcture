import requests
import pandas as pd 
import time 
import json

from datetime import datetime

GOSCORER_URL = "https://api.goscorer.com/api/v3/getSV3?key=1194"
COMMENTARY_URL= "https://content.crickapi.com/commentary/v2/getBallFeeds"
commentary_payload = {
    "matchKey":"1194",
    "lastDocId": None,
    "filters": {}
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

commentary_response = requests.post(
    COMMENTARY_URL,
    json=commentary_payload,headers=headers
)

commentry_data = commentary_response.json()
print(type(commentry_data))
print(commentry_data[0].items())

response = requests.get(GOSCORER_URL,headers=headers)
data = response.json()
print(type(data))
print(data.items())
print(json.dumps(data, indent=4))
print(response.text)






