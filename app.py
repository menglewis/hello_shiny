import logging
import sys

from flask import Flask, render_template, request

logging.basicConfig(stream=sys.stdout)
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        message = request.form['message']
        times = request.form['times']

        for i in range(0, int(times)):
            log_message = message + ' ' + str(i)
            logging.error(log_message)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3838)
