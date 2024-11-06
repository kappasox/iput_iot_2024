#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

# Sample Implemantation of IPUT Course 
# IoT Device Programming 2 (2024 Winter)
# International Professional University of Technology in Tokyo
# Week 05
#
# MCP3208 and MCP3008 Class Library 
#
# Oct. 26, 2024 (Michiharu Takemoto)
#

# MIT License
# 
# Copyright (c) 2021 Michiharu Takemoto <takemoto.development@gmail.com>
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
# 

import time
import datetime

import spidev

Vref = 3.334  # need to check the actual voltage with a tester
spi = spidev.SpiDev()
spi.open(0, 0)  # bus0, cs0
spi.max_speed_hz = 1000000  

# If you heva MCP3008, please use this.
def readMCP3008(channel):
    adc = spi.xfer2([1, (8 + channel) << 4, 200])
    data = ((adc[1] & 3) << 8) + adc[2]
    return data

# The students (2021 and later) use MCP3208.
def readMCP3208(channel):
    ch_b2 = ((channel & 4) >> 2) & 1
    ch_b1 = ((channel & 2) >> 1) & 1
    ch_b0 = channel & 1
#    print("channel = 0b%d%d%d" %(ch_b2, ch_b1, ch_b0))
    
    cmd1 = 0b000_00110 | ch_b2
    cmd2 = ((ch_b1 << 1) | ch_b0) << 6
    cmd3 = 0
#    print("cmd = %x %x %x" %(cmd1, cmd2, cmd3))

    adc = spi.xfer2([cmd1, cmd2, cmd3])
#    print("adc[0] = %x" %adc[0])
#    print("adc[1] = %x" %adc[1])
#    print("adc[2] = %x" %adc[2])
    data = ((adc[1] & 0b0000_1111) << 8) + adc[2]
    return data

if '__main__' == __name__ :
    mcp3208_0 = 0
    dev_0 = 0

    try:
        while True:
            try:
                mcp3208_0 = readMCP3208(channel=0)
    #            print("mcp3208_0: %0x (%d)" %(mcp3208_0, mcp3208_0))
                dev_0 = (mcp3208_0 * Vref) / float(4096)
                print("dev_0: %f V (max=%f)" % (dev_0, Vref))

            except OSError:
                print("MCP3208: error, but we ignore it.: "\
                      + str(datetime.datetime.now()))
                time.sleep(3)

            time.sleep(1)

    except KeyboardInterrupt:
        print('Ctrl-C is hit!')

