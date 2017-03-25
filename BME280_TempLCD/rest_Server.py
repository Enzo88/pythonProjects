from flask import Flask, jsonify
from temp_Lcd_Main import *
import temp_Lcd_Main
import json
app = Flask(__name__)


@app.route('/getSensorData', methods=['GET'])
def get_sensor_data():
    """Get data from BME sensor"""
    sensor = BME280(mode=BME280_OSAMPLE_8)
    return json.dumps(temp_Lcd_Main.read_data(sensor).__dict__)

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=8080)
