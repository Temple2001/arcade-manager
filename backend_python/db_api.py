from pymongo import MongoClient
import datetime
import traceback

# 패키지 설치
# pip install pymongo

class MongoDB_API:
    def __init__(self):
        self.client = MongoClient(host='localhost', port=27017)
        self.log_db = self.client['ArcadeData']['log']

    def add_log(self, user_name, v_id, progress_time, arcade_type):
        try:
            content = {
                'log_time': datetime.datetime.utcnow(),
                'user_name': user_name,
                'v_id': v_id,
                'check_time': progress_time,
                'arcade_type': arcade_type,
            }
            post_id = self.log_db.insert_one(content).inserted_id
            print(f'[OK] 새 데이터가 등록되었습니다. post_id : "{post_id}"')
            return None
        except:
            print(f'[Error] DB 데이터 추가 에러\n{traceback.format_exc()}')
            return '[Failed] DB 데이터 추가 실패'
    
    def find_log(self):
        return self.log_db.find({}, {'_id': False}).sort('log_time')