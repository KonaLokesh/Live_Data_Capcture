import requests
import pandas as pd 
import time 
import json

from datetime import datetime

API_URL = "https://api.goscorer.com/api/v3/getSV3?key=118W"
params = {
    "mfkey": "118W",
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"


}
response = requests.get(API_URL,headers=headers)
data = response.json()
print(type(data))
print(data.keys())
print(json.dumps(data, indent=4))
print(response.text)
