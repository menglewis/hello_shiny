import logging
import sys
from flask import Flask, render_template, request, jsonify

logging.basicConfig(stream=sys.stdout)
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/log', methods=['POST'])
def log():
    data = request.get_json()
    message = data['message']
    times = data['times']
    for i in range(0, int(times)):
        log_message = message + ' ' + str(i)
        logging.error(log_message)

    return jsonify({'status': 200})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3838)
