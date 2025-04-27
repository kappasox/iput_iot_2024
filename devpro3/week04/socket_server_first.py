#!/usr/bin/env /usr/bin/python3
# -*- coding: utf-8 -*-

# Sample Implemantation of IPUT Course IoT Device Programming 3 (2025 Summer)
# Michiharu Takemoto (takemoto.development@gmail.com)

# 2025/04/23
# Socket Server (Example code for explanation)
#
# NOT MIT License
#

import socket

#SERVER = 'localhost'
SERVER = '127.0.0.1'
WAITING_PORT = 8765

socket_w = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket_w.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

socket_w.bind((SERVER, WAITING_PORT)) 

BACKLOG = 5
socket_w.listen(BACKLOG)

socket_s_r, client_address = socket_w.accept()
print('Connection from ' + str(client_address) + " has been established.")

data_s_str = 'Hello! I am a server.'
data_s = data_s_str.encode('utf-8')
socket_s_r.send(data_s)
print('Sent: ' + data_s_str)

data_r = socket_s_r.recv(1024)
data_r_str = data_r.decode('utf-8')
print('Received: ' + data_r_str)
           
socket_w.close()
