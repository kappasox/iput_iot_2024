#!/usr/bin/env /usr/bin/python3
# -*- coding: utf-8 -*-

# Sample Implemantation of IPUT Course IoT Device Programming 3 (2024 Summer)
# Michiharu Takemoto (takemoto.development@gmail.com)
# 2024/05/10
#
# Examples of multiple access with multi-threads
#
#
# NOT MIT License
#

import time
import random
import threading

def print_x_and_wait(t_number):
    global x

    head_blank = ' ' * t_number * 10

    y = x
    print('t%d' %t_number + head_blank + ': x=%d' %x)
    wait_time = random.randint(1, 5)
    print('t%d' %t_number + head_blank + ':  waiting %d sec.' %wait_time)
    time.sleep(wait_time)

    y = y + 1

    x = y
    print('t%d' %t_number + head_blank + ':   ->x=%d' %x)

    wait_time = random.randint(1, 5)
    print('t%d' %t_number + head_blank + ':    waiting %d sec.' %wait_time)
    time.sleep(wait_time)


def single_thread_test():
    print_x_and_wait(1)
    print_x_and_wait(2)
    print_x_and_wait(3)
    print_x_and_wait(4)


def multi_thread_test():
    global x

    t1 = threading.Thread(target=print_x_and_wait, args=(1,))
    t1.start()
    time.sleep(1)

    t2 = threading.Thread(target=print_x_and_wait, args=(2,))
    t2.start()
    time.sleep(1)
    
    t3 = threading.Thread(target=print_x_and_wait, args=(3,))
    t3.start()
    time.sleep(1)
    
    t4 = threading.Thread(target=print_x_and_wait, args=(4,))
    t4.start()
    time.sleep(10)
    
    
x = 10

print('Single-thread')
print('x=%d' %x)
single_thread_test()
print('x=%d' %x)

print()
print('Multi-thread')
x = 10

print('x=%d' %x)
multi_thread_test()
print('x=%d' %x)