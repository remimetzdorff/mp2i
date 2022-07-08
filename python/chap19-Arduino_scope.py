#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  4 12:08:47 2022

@author: remimetzdorff
"""

import matplotlib.pyplot as plt
import numpy as np
import serial

plt.ion()
fig=plt.figure()

i = 0
x, y = [], []
ser = serial.Serial('/dev/cu.usbmodem1434301',9600)
ser.close()
ser.open()
while True:
    data = ser.readline()
    x.append(i)
    y.append(data.decode())

    plt.scatter(i, float(data.decode())/1024*5, color="C0")
    i += 1
    plt.show()
    plt.pause(0.0001)
    plt.ylim(-1e-3,5e-3)