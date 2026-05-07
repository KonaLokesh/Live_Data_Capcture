

import requests
import pandas as pd 
import time 

from datetime import datetime
API_URL = "https://api.goscorer.com/api/v3/getSV3?key=118V"
params = {
    "mfkey": "118V",
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    
}