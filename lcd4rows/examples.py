# requires RPi_I2C_driver.py
import RPi_I2C_driver
from time import *
import socket
import netifaces as ni
ni.ifaddresses('eth0')

mylcd = RPi_I2C_driver.lcd()
mylcd.lcd_display_string("IP Address:", 1)
mylcd.lcd_display_string(ni.ifaddresses('eth0')[2][0]['addr'], 2)
#sleep(1)
#mylcd.backlight(0)
