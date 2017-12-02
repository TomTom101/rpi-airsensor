from flask import Flask
from airsensor import Airsensor

sensor = Airsensor()

app = Flask(__name__)

@app.route('/')
def index():
    return sensor.test()

@app.route('/read')
def get_sensor():
    return sensor.read()

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
