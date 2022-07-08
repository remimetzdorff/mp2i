#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 23 19:20:33 2022
Réversibilité et irréversibilité
@author: remimetzdorff
"""

import numpy as np
import matplotlib.pyplot as plt

N = 1     # Nombre d'étapes
tau = 1   # Temps caractéristique

def T(t, t0, T1, T2, tau=1):
    return T1 + (T2 - T1) * (1 - np.exp(-(t-t0)/tau))
def Tr(t, t0, T1, T2, tau=1):
    return T2 + (T1 - T2) * (np.exp(-(t-t0)/tau))

Ts = np.linspace(10, 20, N+1)
ts = np.linspace(0, 5*N*tau, N+1)
for i in range(N):
    t = np.linspace(ts[i], ts[i+1], int(1000/N)+2)
    plt.plot(t, T(t, ts[i], Ts[i], Ts[i+1], tau), "C0")
    if True: # Transformation inverse
        plt.plot(t, Tr(t, ts[i], Ts[N-i], Ts[N-i-1], tau), "C1", alpha=.5)

plt.xlabel("Temps")
plt.ylabel("Température")
plt.show()