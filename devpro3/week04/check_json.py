#!/usr/bin/env /usr/bin/python3
# -*- coding: utf-8 -*-

# Sample Implemantation of IPUT Course IoT Device Programming 3 (2022 Summer)
# Michiharu Takemoto (takemoto.development@gmail.com)
# 2023/05/01
#
# Examples to convert Python list to/from JSON (string)
#
#
# NOT MIT License
#

import json

print("Check: string (JSON) -> list (Python)")
data1 = '[{"tempe_dht_1": 27.0, "humid_dht_1": 50.0}]'
print("data1:", type(data1), data1)
data1_python = json.loads(data1)
print("data1_python", type(data1_python), data1_python)

print()
print("Check: list (Python) -> string (JSON) ")
data2 = [{'tempe_dht_1': 33.1, 'humid_dht_1': 60.0}]
print("data2:", type(data2), data2)
data2_json = json.dumps(data2)
print("data2_json:", type(data2_json), data2_json)

print()
print("Check: string (JSON) -> list (Python)")
data3 = '[{"tempe_dht_1": 27.0, "humid_dht_1": 50.0}, {"tempe_dht_1": 28.0, "humid_dht_1": 51.0}, {"tempe_dht_1": 32, "humid_dht_1": 50.0}]'
print("data1:", type(data3), data3)
data3_python = json.loads(data3)
print("data3_python", type(data3_python), data3_python)

print()
print("Check: list (Python) -> string (JSON) ")
data4 = [{'tempe_dht_1': 33.1, 'humid_dht_1': 60.0}, {'tempe_dht_1': 30.2, 'humid_dht_1': 44.0}, {'tempe_dht_1': 30, 'humid_dht_1': 50}]
print("data4:", type(data4), data4)
data4_json = json.dumps(data4)
print("data4_json:", type(data4_json), data4_json)

print()
print("Check: list (Python) -> string (JSON) ")
data5 = ['a', 'b']
print("data5:", type(data5), data5)
data5_json = json.dumps(data5)
print("data4_json:", type(data5_json), data5_json)

print()
print("Check: dict (Python) -> string (JSON) ")
data6 = { 
    "dht_1": {'tempe_dht_1': 33.1, 'humid_dht_1': 60.0}, 
    "dht_2": {'tempe_dht_1': 30.2, 'humid_dht_1': 44.0}, 
    "dht_3": {'tempe_dht_1': 30, 'humid_dht_1': 50}
} 
print("data5:", type(data6), data6)
data6_json = json.dumps(data6)
print("data6_json:", type(data6_json), data6_json)



