#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 21:23:57 2022
Circuit RLC
@author: remimetzdorff
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#########################
# MODÉLISATION DU CIRCUIT
#########################
# Circuit RLC série alimenté par le signal sinusoïdal e d'un GBF,
# On mesure de la tension s aux bornes du condensateur
R = 100     # résistance en ohms
L = 11e-3   # inductance en henry
C = 10e-9   # capacité en farad
f = 1e3     # fréquence du GBF
V0  = [0,0] # conditions initiales pour la résolution

def e(t):
    # signal du GBF
    return 1*np.cos(2*np.pi*f*t)

def rlc(V,t):
    # fonction associée à l'équation différentielle
    s, ds = V
    dds = (e(t) - s) / (L*C) - R/L * ds
    dV = [ds, dds]
    return dV

########################################
# RÉSOLUTION ET REPRÉSENTATION GRAPHIQUE
########################################
t = np.linspace(0,3e-3,1000) # temps t en seconde
V = odeint(rlc, V0, t)
s = V[:,0]                   # tension aux bornes de C

plt.title("Réponse d'un circuit RLC à une excitation sinusoïdale")
plt.plot(t*1e3,e(t),label="$e(t)$")
plt.plot(t*1e3,s,label="$s(t)$")
plt.xlabel("Temps (ms)")
plt.ylabel("Tension (V)")
plt.legend()
plt.show()