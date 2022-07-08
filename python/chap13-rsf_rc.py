#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 21:14:50 2022
Circuit RC
@author: remimetzdorff
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#########################
# MODÉLISATION DU CIRCUIT
#########################
# Circuit RC série alimenté par le signal sinusoïdal e d'un GBF,
# On mesure de la tension s aux bornes du condensateur
R = 1e3   # résistance en ohms
C = 10e-9 # capacité en farad
tau = R*C # temps caractéristique en seconde
f = 100e3 # fréquence du GBF
V0  = [1] # CI

def e(t):
    # signal du GBF
    return 1*np.cos(2*np.pi*f*t)
    
def rc(V,t):
    # fonction associée à l'équation différentielle
    s = V[0]
    ds = (e(t) - s) / tau
    dV = [ds]
    return dV

########################################
# RÉSOLUTION ET REPRÉSENTATION GRAPHIQUE
########################################
t = np.linspace(0,1e-4,1000) # temps t en seconde
V = odeint(rc, V0, t)
s = V[:,0]                   # tension aux bornes de C

plt.title("Réponse d'un circuit RC à une excitation sinusoïdale")
plt.plot(t*1e3,e(t),label="$e(t)$")
plt.plot(t*1e3,s,label="$s(t)$")
plt.xlabel("Temps (ms)")
plt.ylabel("Tension (V)")
plt.legend()
plt.show()