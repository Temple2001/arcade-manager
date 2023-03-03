from flask import Flask, request, jsonify
from flask_cors import CORS
from db_api import MongoDB_API

app = Flask(__name__)
CORS(app, resources={r'*':{'origins': 'http://localhost:3000'}})
#app.debug = True
app.config['JSON_AS_ASCII'] = False
db_api = MongoDB_API()

@app.route('/log-data', methods=['GET', 'POST'])
def main_page():
    if request.method == 'GET':
        res = list(db_api.find_log())
        for data in res:
            data['log_time'] = str(data['log_time']).split('.', 2)[0]
        return jsonify(res)

    if request.method == 'POST':
        user_name = request.args.get('username')
        v_id = request.args.get('vid')
        progress_time = request.args.get('time')
        arcade_type = request.args.get('type')

        db_api.add_log(user_name, v_id, progress_time, arcade_type)
        return jsonify({'msg': 'Insert Completed'})


if __name__ == '__main__':
    app.run()