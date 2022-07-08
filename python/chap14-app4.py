#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 19:12:12 2022
Application 4
@author: remimetzdorff
"""

import numpy as np
import matplotlib.pyplot as plt

f0 = 10
fe = 1

def H(f):
    return 1 / (1+1j*f/f0)

def Hhp(f):
    return 1j*f/f0 / (1+1j*f/f0)

H = Hhp

def G(f):
    return np.abs(H(f))

def phi(f):
    return np.angle(H(f))

t = np.linspace(0,3/fe,1000)

a0 = .5
a1 = 1
a10 = .25

e0 = a0 * np.ones(len(t))
e1 = a1 * np.cos(2*np.pi*fe*t)
e10= a10*np.cos(2*np.pi*10*fe*t)
e  = e0 + e1 + e10

s0 = e0 * G(0)
s1 = a1 * G(fe)*np.cos(2*np.pi*fe*t + phi(fe))
s10= a10 * G(10*fe)*np.cos(2*np.pi*10*fe*t + phi(10*fe))
s  = s0 + s1 + s10

plt.plot(t,e)
plt.plot(t,s)

plt.xlabel("Temps")
plt.ylabel("Signal")
plt.show()