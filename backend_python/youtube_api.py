import requests
import json
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
from urllib.parse import urlparse, parse_qs
import traceback

class YoutubeAPI:

    def __init__(self):
        load_dotenv(verbose=True)
        self.API_KEY = os.getenv('API_KEY')
    
    def find_video(self, keyword):
        params = {
            'q': keyword,
            'part': 'snippet',
            'key': self.API_KEY,
            'maxResults': 3,
            'type': 'video',
            'order': 'date',
        }

        response = requests.get('https://www.googleapis.com/youtube/v3/search', params=params)
        res_json = response.json()
        if response.status_code != 200:
            print('[Error] find_video 에러, 생방송 video를 찾지 못함.')
            print(json.dumps(res_json, indent=2))
            return None, '[Failed] 해당 생방송 video를 찾지 못했습니다.'
        
        search_list = res_json['items']
        for video in search_list:
            if video['snippet']['liveBroadcastContent'] == 'live':
                return video['id']['videoId'], None
            
    def url_parse(self, url):
        try:
            parsed_url = urlparse(url)
            v_id = parse_qs(parsed_url.query)['v'][0]
            return v_id, None
        except:
            print(f'[Error] urlparse 에러\n{traceback.format_exc()}')
            return None, '[Failed] 올바른 URL을 입력하세요.'

    def time_check(self, v_id):
        try:
            params = {
                'part': 'snippet',
                'id': v_id,
                'key': self.API_KEY,
            }

            response = requests.get('https://www.googleapis.com/youtube/v3/videos', params=params)
            res_json = response.json()

            start_time_utc = res_json['items'][0]['snippet']['publishedAt']

            start_time_utc = datetime.strptime(start_time_utc, '%Y-%m-%dT%H:%M:%SZ')
            progress_time = str(datetime.now() - start_time_utc).split('.', 2)[0]
            return progress_time, None
        except:
            print(f'[Error] API 호출 에러\n{traceback.format_exc()}')
            return None, '[Failed] 유효하지 않은 동영상입니다.'