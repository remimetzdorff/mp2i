#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 19:18:39 2022
TD14 exo 4
@author: remimetzdorff
"""

import numpy as np
import matplotlib.pyplot as plt

def H1(f,f0=1e2, Q=2):
    return -(f/f0)**2 / (1 - (f/f0)**2 + 1j * (f/f0/Q))

def H2(f,f0=1e3, Q=1):
    return 2*(1 - (f/f0)**2) / (1 - (f/f0)**2 + 1j * (f/f0/Q))

def H3(f,f0=1e6, Q=1):
    return 1j * f/f0 / (1 + 1j * (f/f0))

def H4(f,f0=10e3, Q=.1):
    return 1 / (1 - (f/f0)**2 + 1j * (f/f0/Q))

def G(f, H):
    return np.abs(H(f))

def phi(f, H):
    return np.angle(H(f))

E0 = 1
f      = 1e3
fn     = [ 0,  f,    10*f,    100*f]
cn     = [E0, E0,      E0,       E0]
phin   = [ 0,  0, np.pi/4, -np.pi/3]

def e(t):
    output = 0
    for n in range(4):
        output += cn[n] * np.cos(2*np.pi*fn[n] * t + phin[n])    
    return output

def s(t, H):
    output = 0
    for n in range(4):
        c     = cn[n] * G(fn[n], H)
        phase = phin[n] + phi(fn[n], H)
        output += c * np.cos(2*np.pi*fn[n] * t + phase)    
    return output

t = np.linspace(0, 2/f, 10000)
plt.plot(t*1e3, e(t), label="e(t)", alpha=.5)
plt.plot(t*1e3, s(t, H3), label="s(t)")

plt.xlabel("Temps (ms)")
plt.ylabel("Signal")
plt.legend()
plt.grid()
plt.show()