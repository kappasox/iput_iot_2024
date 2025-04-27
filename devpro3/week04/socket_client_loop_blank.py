#!/usr/bin/env /usr/bin/python3
# -*- coding: utf-8 -*-

# Sample Implemantation of IPUT Course IoT Device Programming 3 (2022 Summer)
# Michiharu Takemoto (takemoto.development@gmail.com)
#
# 2022/05/10
# Socket Client WITH BLANK
#
# NOT MIT License
#

import sys

SERVER = 'localhost'
WAITING_PORT = 8765
MESSAGE_FROM_CLIENT = "Hello, I am a client."

WAIT_INTERVAL = 5

def client_test(hostname_v1 = SERVER, waiting_port_v1 = WAITING_PORT, message1 = MESSAGE_FROM_CLIENT):
    import socket
    import time

    node_s = hostname_v1
    port_s = waiting_port_v1

    try:
        count = 0
        while True:

            # socoket for receiving and sending data
            # AF_INET     : IPv4
            # SOCK_STREAM : TCP
            socket_r_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket_r_s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            print("node_s:", node_s,  " port_s:", str(port_s))
            socket_r_s.XXXX((node_s, port_s))
            print('Connecting to the server. '
                + 'node: ' + node_s + '  '
                + 'port: ' + str(port_s))

            data_s_str = message1
            # data_s = bytes(data_s_str, encoding = 'utf-8')
            data_s = data_s_str.encode('utf-8')
            socket_r_s.send(data_s)
            print('I (a client) have just sent data __' 
                + data_s_str 
                + '__ to the server ' + node_s + ' .')

            socket_r_s.XXXX()

            time.sleep(WAIT_INTERVAL)

            count = count + 1
            if count > 5:
                break

    except KeyboardInterrupt:
        print("Ctrl-C is hit!")
        print("End of this client.")


if __name__ == '__main__':
    print("Start if __name__ == '__main__'")
    
    sys_argc = len(sys.argv)
    count = 1
    hostname_v = SERVER
    waiting_port_v = WAITING_PORT
    message_v = MESSAGE_FROM_CLIENT

    while True:
        print(count, "/", sys_argc)
        if(count >= sys_argc):
            break

        option_key = sys.argv[count]
        #print(option_key)
        if ("-h" == option_key):
            count = count + 1
            hostname_v = sys.argv[count]
            #print(option_key, hostname_v)
        if ("-p" == option_key):
            count = count + 1
            waiting_port_v = int(sys.argv[count])
            #print(option_key, port_v)
        if ("-m" == option_key):
            count = count + 1
            message_v = sys.argv[count]
            #print(option_key, message_v)

        count = count + 1

    print(hostname_v)
    print(waiting_port_v)
    print(message_v)

    client_test(hostname_v, waiting_port_v, message_v)
    