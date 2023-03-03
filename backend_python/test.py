import requests
import os
from dotenv import load_dotenv
from urllib import parse
import json

load_dotenv(verbose=True)

params = {
    'q': 'AmuseTown+SDVX+Valkyrie+model',
    'part': 'snippet',
    'key': os.getenv('API_KEY'),
    'maxResults': 3,
    'type': 'video',
    'order': 'date',
}

print(parse.quote('AmuseTown SDVX Valkyrie model'))
response = requests.get('https://www.googleapis.com/youtube/v3/search', params=params)
res_json = response.json()

print(json.dumps(res_json, indent=2))