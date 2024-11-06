#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# IPUT IoT Device Programming 2 (2024)
# International Professional University of Technology in Tokyo
# Sample Coode of mcp3208_mpc3008.py with adafruit_ssd1306

#
# Nov. 5, 2024 (Michiharu Takemoto)
#

# MIT License
# 
# Copyright (c) 2022 Michiharu Takemoto <takemoto.development@gmail.com>
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# 

# You need AdaFruit's library
# $ pip3 install adafruit-circuitpython-ssd1306
# .
# And you have to have mcp3208_mcp3008.py in the same
# directory.


import time
import datetime

import board
import adafruit_ssd1306

WIDTH = 128
#HEIGHT = 32  # Change to 64 if needed
HEIGHT = 64  # Change to 64 if needed
BORDER = 5

from mcp3208_mcp3008 import readMCP3208

def js_calibration():
    print('Calibration')

    print('Wait! Checking the center')
    count = 0
    jx_c_sum = 0
    jy_c_sum = 0
    while True:
        js_x = readMCP3208(channel=2)
        js_y = readMCP3208(channel=3)
        jx_c_sum = jx_c_sum + js_x
        jy_c_sum = jy_c_sum + js_y
        time.sleep(0.1)
        count = count + 1
        if ((count % 10) == 0):
            print(int(count / 10))
        if (count > 100):
            break
    js_x_center = int(jx_c_sum / 100)
    js_y_center = int(jy_c_sum / 100)
    print('End of checking the center!')

    js_x_max = 2048
    js_x_min = 2048
    js_y_max = 2048
    js_y_min = 2048
    print('Start!')
    count = 0
    while True:
        js_x = readMCP3208(channel=2)
        js_y = readMCP3208(channel=3)
        if (js_x > js_x_max):
            js_x_max = js_x
        if (js_x < js_x_min):
            js_x_min = js_x
        if (js_y > js_y_max):
            js_y_max = js_y
        if (js_y < js_y_min):
            js_y_min = js_y
        time.sleep(0.1)
        count = count + 1
        if ((count % 10) == 0):
            print(int(count / 10))
        if (count > 100):
            break

    print('Finished the calibration!')

    print('Joystick X: %d - %d - %d' %(js_x_min, js_x_center, js_x_max))
    print('Joystick Y: %d - %d - %d' %(js_y_min, js_y_center, js_y_max))

    return js_x_min, js_x_center, js_x_max, js_y_min, js_y_center, js_y_max

if '__main__' == __name__ :
    i2c_now = board.I2C()
    instance_ssd1306 = adafruit_ssd1306.SSD1306_I2C(width=WIDTH, height=HEIGHT, i2c=i2c_now, addr=0x3c)

    js_x = 0
    js_y = 0

    js_x_max = 2048
    js_y_max = 2048
    js_x_center = 2048
    js_y_center = 2048
    js_x_min = 2048
    js_y_min = 2048

    js_x_min, js_x_center, js_x_max, js_y_min, js_y_center, js_y_max = js_calibration()
    js_x_width = js_x_max - js_x_center # ここを何とかしたい
    js_y_width = js_y_max - js_y_center # ここを何とかしたい

    dot_x_max = WIDTH - 1
    dot_x_min = 1
    dot_y_max = HEIGHT - 1
    dot_y_min = 1
    dot_x = int(WIDTH / 2)
    dot_y = int(HEIGHT / 2)

    try:
        while True:
            try:
                js_x = readMCP3208(channel=2)
                js_y = readMCP3208(channel=3)

                diff_x = (js_x - js_x_center) / js_x_width # ここを何とかしたい
                diff_y = (js_y - js_y_center) / js_y_width # ここを何とかしたい
                print(diff_x, diff_y)

                dot_x = dot_x + int(diff_x * 2)
                if (dot_x > dot_x_max):
                    dot_x = dot_x_min
                if (dot_x < dot_x_min):
                    dot_x = dot_x_max

                dot_y = dot_y + int(diff_y * 2)
                if (dot_y > dot_y_max):
                    dot_y = dot_y_min
                if (dot_y < dot_y_min):
                    dot_y = dot_y_max

                instance_ssd1306.fill(0)
                instance_ssd1306.pixel(dot_x, dot_y, 1)
                instance_ssd1306.show()

            except OSError:
                print("MCP3208: error, but we ignore it.: "\
                      + str(datetime.datetime.now()))
                time.sleep(3)

            time.sleep(0.1)

    except KeyboardInterrupt:
        print('Ctrl-C is hit!')
        print('Program ends!')
