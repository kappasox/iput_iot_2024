#!/usr/bin/env /usr/bin/python3
# -*- coding: utf-8 -*-

# Sample Implemantation of IPUT Course IoT Device Programming 3 (2023 Summer)
# Michiharu Takemoto (takemoto.development@gmail.com)
#
# 2025/04/27
# Get temperature and humidity data from DHT11
# Loop vesion with exception
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

dht11_instance = dht11.DHT11(pin=26)

WAIT_INTERVAL = 2
WAIT_INTERVAL_RETRY = 5

def get_dht_data():
    tempe = 200.0 # unnecessary value-setting
    hum = 100.0 # unnecessary value-setting

    try:
        tempe, hum, check = dht11_instance.read()
        print('Last valid input: ' + str(datetime.datetime.now()))
        print('Temperature: %-3.1f C' % tempe)
        print('Humidity: %-3.1f %%' % hum)
    
    except dht11.DHT11CRCError:
        print('DHT11CRCError: ' + str(datetime.datetime.now()))
        time.sleep(WAIT_INTERVAL_RETRY)
        raise(dht11.DHT11CRCError)

    except dht11.DHT11MissingDataError:
        print('DHT11MissingDataError: ' + str(datetime.datetime.now()))
        time.sleep(WAIT_INTERVAL_RETRY)
        raise(dht11.DHT11MissingDataError)

    return float(tempe), float(hum)

def test_get_dht_data():
    count = 0 
    tempe = 40.0
    humid = 85.0
    while True:

        try:
            tempe, humid = get_dht_data()
            now_str = str(datetime.datetime.now())
            print("Temperature: %f  Humidity: %f" % (tempe, humid), now_str)
        except dht11.DHT11CRCError:
            print("DHT11CRCError in get_dht_data(). Let us ignore it!")
            time.sleep(WAIT_INTERVAL_RETRY)
        except dht11.DHT11MissingDataError:
            print("DHT11MissingDataError in get_dht_data(). Let us ignore it!")
            time.sleep(WAIT_INTERVAL_RETRY)

        time.sleep(WAIT_INTERVAL)
        count = count + 1
        if (count > 5):
            break

if __name__ == '__main__':
    print("Start if __name__ == '__main__'")
    test_get_dht_data()
