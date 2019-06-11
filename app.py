import logging
from datetime import datetime
import json
import sys
from flask import Flask, render_template, request, jsonify


class LevelFilter(logging.Filter):
    def __init__(self, *args):
        self.levels = args

    def filter(self, record):
        return record.levelno in self.levels


h1 = logging.StreamHandler(sys.stdout)
f1 = LevelFilter(logging.DEBUG, logging.INFO, logging.WARNING)
h1.addFilter(f1)

h2 = logging.StreamHandler(sys.stderr)
f2 = LevelFilter(logging.ERROR, logging.CRITICAL)
h2.addFilter(f2)

rootLogger = logging.getLogger()
rootLogger.addHandler(h1)
rootLogger.addHandler(h2)

logger = logging.getLogger('test')
logger.setLevel(logging.DEBUG)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/log', methods=['POST'])
def log():
    data = request.get_json()
    message = data['message']
    level = data['level']

    json_message = {
        'message': message,
        'level': level,
        'timestamp': datetime.utcnow().isoformat(),
    }
    getattr(logger, level)(json.dumps(json_message))

    return jsonify({'message': 'Logged message successfully'})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3838)
