#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 19:12:12 2022
Application 5
@author: remimetzdorff
"""

import numpy as np
import matplotlib.pyplot as plt

f0 = 2000
fe = 100

def H(f):
    return 1 / (1+1j*f/f0)

def G(f):
    return np.abs(H(f))

def phi(f):
    return np.angle(H(f))

t = np.linspace(0,2/fe,100000)

a0 = 5
a1 = 1
a2 = 2
a3 = 10

e0 = a0 * np.ones(len(t))
e1 = a1 * np.cos(2*np.pi*fe*t)
e2 = a2 * np.cos(2*np.pi*20*fe*t)
e3 = a3 * np.cos(2*np.pi*2000*fe*t)

s0 = e0 * G(0)
s1 = a1 * G(fe) * np.cos(2*np.pi*fe*t + phi(fe))
s2 = a2 * G(20*fe) * np.cos(2*np.pi*20*fe*t + phi(20*fe))
s3 = a3 * G(2000*fe) * np.cos(2*np.pi*2000*fe*t + phi(2000*fe))

e = e0 + e1 + e2 + e3
s = s0 + s1 + s2 + s3

plt.plot(t,e)
plt.plot(t,s)

plt.xlabel("Temps")
plt.ylabel("Signal")
plt.show()