#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 23:29:11 2022
Nyquist-Shannon
@author: remimetzdorff
"""

import numpy as np
import matplotlib.pyplot as plt

f = 1e3
fe = 950

t = np.linspace(0,20e-3, 2**12)
y = np.sin(2*np.pi*f*t)
plt.plot(t*1e3,y)

t = np.arange(0,20e-3, 1/fe)
y = np.sin(2*np.pi*f*t)
plt.plot(t*1e3,y ,"-o", label="fe="+str(0.95)+" kHz")

plt.xlabel("Temps (ms)")
plt.ylabel("Amplitude (V)")
plt.legend(loc="upper right")

plt.show()