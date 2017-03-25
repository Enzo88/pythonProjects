from flask import Flask, jsonify
from tempLcdMain import *
import tempLcdMain
import json
app = Flask(__name__)


@app.route('/getSensorData', methods=['GET'])
def get_sensor_data():
    """Get data from BME sensor"""
    sensor = BME280(mode=BME280_OSAMPLE_8)
    return json.dumps(tempLcdMain.read_data(sensor).__dict__)

if __name__ == '__main__':
    app.run(debug=True)
