#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 23:11:20 2022
TD22 - Moteur de Stirling (https://fr.wikipedia.org/wiki/Moteur_Stirling)
@author: remimetzdorff
"""

import numpy as np
import matplotlib.pyplot as plt

V1m, V1M = 0, 0.0001
V2m, V2M = 0, 0.0001

def V1(t):
    return (V1M-V1m) * np.cos(2*np.pi*t) / 2 + (V1M + V1m) / 2

def V2(t):
    return (V2M-V2m) * np.sin(2*np.pi*t) / 2 + (V2M + V2m) / 2

def V(t):
    return V1(t) + V2(t)

t = np.linspace(0, 1, 1000)
V_reel = V(t)
Vm, VM = min(V_reel), max(V_reel)

T1, T2 = 300, 1000
R = 8.314
n = 1e5 * Vm / R / T1
m = n * 29e-3

def P(t):
    n1 = n * T2/V2(t) / ( T1/V1(t) + T2/V2(t) )
    return n1 * R * T1 / V1(t)

P_reel = P(t)

t = np.linspace(0, 1, 1000)
P_reel, V_reel = P(t), V(t)
Vm, VM = min(V_reel), max(V_reel)
Pa, Pb = n*R*T1/Vm, n*R*T2/Vm
Pc, Pd = n*R*T2/VM, n*R*T1/VM

v     = np.linspace(Vm, VM)
v_rev = np.linspace(VM, Vm)

Pbc = Pb*Vm / v
Pda = Pa*Vm / v_rev

V_mod = np.array([Vm, Vm] + list(v) + [VM, VM] + list(v_rev))
P_mod = np.array([Pa, Pb] + list(Pbc) + [Pc, Pd] + list(Pda))

plt.plot(V_reel/m, P_reel*1e-5, label="cycle 'réel'")
plt.plot(V_mod/m, P_mod*1e-5, label="cycle modèle")
plt.xlabel("Volume massique $v$ ($\\rm{kg \cdot m^{-3}}$)")
plt.ylabel("Pression (bar)")
plt.title("Diagramme de Clapeyron d'un cycle de Stirling")
plt.xlim(0,6)
plt.ylim(0,4)
plt.legend()