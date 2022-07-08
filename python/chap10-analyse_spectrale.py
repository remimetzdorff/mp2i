#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 11:37:12 2022
Analyse spectrale
@author: remimetzdorff
"""

import numpy as np
import matplotlib.pyplot as plt

def signal_carre(t,f=1,N=1):
    s = np.zeros(len(t))
    for n in range(1,N+1):
        if n%2 != 0:
            an = 4/np.pi/n
            sn = an * np.cos(2*np.pi * n * f * t - np.pi/2)
            s += sn
            plt.plot(t, sn, "C0", alpha=0.25)
    return s

def signal_triangle(t,f=1,N=1):
    s = np.zeros(len(t))
    for n in range(1,N+1):
        if n%2 != 0:
            an = 8 / np.pi**2 * (-1) ** ((n-1) / 2) / n**2
            sn = an * np.sin(2*np.pi * n * f * t)
            s += sn
            plt.plot(t, sn, "C0", alpha=0.25)
    return s



t = np.linspace(0,5,1001)

plt.plot(t, signal_triangle(t,N=15))
plt.xlabel("Temps $t$ (s)")
plt.ylabel("Signal $s(t)$")