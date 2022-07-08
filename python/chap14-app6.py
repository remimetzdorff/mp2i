#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 09:20:34 2022
Chapitre 14 : application 6
@author: remimetzdorff
"""

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0,.02,10000)

e = np.cos(2*np.pi*100*t)\
    + np.cos(2*np.pi*1000*t)\
    + .25 * np.cos(2*np.pi*10000*t)

s = .1 * np.cos(2*np.pi*100*t + np.pi/2)\
    + 1/np.sqrt(2) * np.cos(2*np.pi*1000*t + np.pi/4)\
    + .25 * np.cos(2*np.pi*10000*t)
    
plt.plot(t*1e3,e)
plt.plot(t*1e3,s)
plt.xlabel("Temps (ms)")
plt.ylabel("Signal")
plt.show()