#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 08:06:29 2022
TD17 exo 10
@author: remimetzdorff
"""

import numpy as np
from scipy.integrate import quad    

n  = 10000
t0 = 5*np.pi/180
tf = np.pi/2

def f(t):
    return 1 / np.sqrt(np.cos(t0) - np.cos(t))

def rect_gauche(f, a, b):
    I = 0
    step = (b-a)/n
    for k in range(n-1):
        I += f(a + k*step)
    return I * step

def rect_droite(f, a, b):
    I = 0
    step = (b-a)/n
    for k in range(n-1):
        I += f(a + (k+1)*step)
    return I * step

def rect_milieu(f, a, b):
    I = 0
    step = (b-a)/n
    for k in range(n-1):
        I += f(a + (k + .5)*step)
    return I * step

def trapeze(f, a, b):
    I = 0
    step = (b-a)/n
    for k in range(n-1):
        I += (f(a + k*step) + f(a + (k+1)*step)) / 2
    return I * step

print(rect_gauche(f, t0, tf))
print(rect_droite(f, t0, tf))
print(rect_milieu(f, t0, tf))
print(trapeze(f, t0, tf))

res, err = quad(f, t0, tf)

