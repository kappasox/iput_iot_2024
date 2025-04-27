#!/usr/bin/env /usr/bin/python3
# -*- coding: utf-8 -*-

# Sample Implemantation of IPUT Course IoT Device Programming 3 (2025 Summer)
# Michiharu Takemoto (takemoto.development@gmail.com)
#
# 2025/04/23
# Socket Client (Example code for explanation)
#
# NOT MIT License
#

import socket

#SERVER = 'localhost'
SERVER = '127.0.0.1'
WAITING_PORT = 8765
   
socket_r_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket_r_s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

socket_r_s.connect((SERVER, WAITING_PORT))

data_r = socket_r_s.recv(1024)
data_r_str = data_r.decode('utf-8')
print('Received: ' + data_r_str)


data_s_str = 'Hello, Server! I am a client.'
data_s = data_s_str.encode('utf-8')
socket_r_s.send(data_s)
print('Sent: ' + data_s_str)
