#!/usr/bin/env /usr/bin/python3
# -*- coding: utf-8 -*-

# Sample Implemantation/Code of IPUT Course IoT Device Programming 3 (2024 Summer)
# Michiharu Takemoto (takemoto.development@gmail.com)
#
# 2023/04/22 how to use matplotlib

import numpy as np
import matplotlib.pyplot as plt

#FILE_DIR = "/home/pi/devpro3/data"
#FILE_DIR = "c:/Users/takemoto/Python/devpro3/week03_matplotlib"
FILE_DIR = "./"
FILENAME = "week03/data_dht11_pseudo.csv"
FULL_FILENAME = FILE_DIR + "/"+ FILENAME

def matplotlib_test():
    data_set = np.loadtxt(
        fname=FULL_FILENAME,
        dtype="float",
        delimiter=",",
    )

    #散布図はplt.scatter
    #list data_setから1組ずつ取り出して描画
    #plt.scatter(x座標の値, y座標の値)
    for data in data_set:
        plt.scatter(data[0], data[1])

    plt.title("DHT11 Data")
    plt.xlabel("Temperature")
    plt.ylabel("Humidity")
    plt.grid()

    plt.show()


if __name__ == '__main__':
    print("Start if __name__ == '__main__'")
    matplotlib_test()
    