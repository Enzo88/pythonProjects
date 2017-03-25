from Adafruit_BME280 import *
import RPi_I2C_driver

class BmeData(object):
    """Data from BME280 sensor"""

    def __init__(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure

    def print_data(self):
        """Write data to string"""
        print 'Temp      = {0:0.3f} C'.format(self.temperature)
        print 'Pressure  = {0:0.2f} hPa'.format(self.pressure)
        print 'Humidity  = {0:0.2f} %'.format(self.humidity)

    def print_data_lcd(self, lcd):
        """Write data to lcd"""
        lcd.lcd_display_string("Temp   = {0:0.2f} C".format(self.temperature), 1)
        lcd.lcd_display_string("Press  = {0:0.2f} hPa".format(self.pressure), 2)
        lcd.lcd_display_string("Humi   = {0:0.2f} %".format(self.humidity), 3)

def read_data(sensor):
    """Read data from sensor"""
    return BmeData(sensor.read_temperature(), sensor.read_humidity(), sensor.read_pressure()/100)

def main():
    """Main"""
    sensor = BME280(mode=BME280_OSAMPLE_8)
    mylcd = RPi_I2C_driver.lcd()
    mylcd.lcd_clear()
    while True:
        try:
            read_data(sensor).print_data_lcd(mylcd)
            time.sleep(2)
        except KeyboardInterrupt:
            mylcd.lcd_clear()
            time.sleep(1)
            mylcd.backlight(0)
            sys.exit()

if __name__ == "__main__":
    main()
