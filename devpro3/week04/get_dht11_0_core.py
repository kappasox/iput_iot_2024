#!/usr/bin/env /usr/bin/python3
# -*- coding: utf-8 -*-

# Sample Implemantation of IPUT Course IoT Device Programming 3 (2025 Summer)
# Michiharu Takemoto (takemoto.development@gmail.com)
#
# 2025/03/07
# Get temperature and humidity data from DHT11/DHT22 
# Only function without exception-raise
#
# NOT MIT License
#

# You have to use dht11_takemoto libraries by
# storing dht11_takemoto.py in the same directory.
# And, you have to install RPi.GPIO by
# $ pip install RPi.GPIO
# . 

import RPi.GPIO as GPIO
import dht11_takemoto as dht11
import time
import datetime

# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

# read data using pin 26
dht11_instance = dht11.DHT11(pin=26)

WAIT_INTERVAL_RETRY = 5

try:
    tempe, hum, check = dht11_instance.read()
    print('Last valid input: ' + str(datetime.datetime.now()))
    print('Temperature: %-3.1f C' % tempe)
    print('Humidity: %-3.1f %%' % hum)
    
except dht11.DHT11CRCError:
    print('DHT11CRCError: ' + str(datetime.datetime.now()))
    time.sleep(WAIT_INTERVAL_RETRY)

except dht11.DHT11MissingDataError:
    print('DHT11MissingDataError: ' + str(datetime.datetime.now()))
    time.sleep(WAIT_INTERVAL_RETRY)


