import os
import sys
import time
from flask import Flask, render_template, request, jsonify


class AppBrokenError(Exception):
    status_code = 500

    def __init__(self, message=None):
        self.message = message

    def to_dict(self):
        return {
            'message': self.message
        }

app = Flask(__name__)
BROKEN = False

@app.route('/', methods=['GET'])
def index():
    if BROKEN:
        raise AppBrokenError('App is broken')
    return render_template('index.html')

@app.route('/override', methods=['GET'])
def override():
    return render_template('index.html')

@app.route('/break', methods=['POST'])
def disable():
    global BROKEN
    data = request.get_json()
    BROKEN = data['broken']
    return jsonify({'message': 'Success'})

delay = os.environ.get('STARTUP_DELAY', None)
if delay:
    time.sleep(int(delay))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3838)
