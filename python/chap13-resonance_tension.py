#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 15:10:37 2022
Résonance en tension aux bornes du condensateur
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
omega0 = 1
Q      = 10
omega  = 1     # pulsation du GBF

def e(t):
    # signal du GBF
    return np.cos(omega * t)

def rlc(V,t):
    # fonction associée à l'équation différentielle
    s, ds = V
    dds = omega0**2 * (e(t) - s) - omega0/Q * ds
    dV = [ds, dds]
    return dV

########################################
# RÉSOLUTION ET REPRÉSENTATION GRAPHIQUE
########################################
t = np.linspace(-10*Q/omega0,5*2*np.pi/omega,1000) # temps t en seconde
V = odeint(rlc, [0,0], t)
s = V[:,0]                   # tension aux bornes de C

plt.title("Résonance en tension aux bornes du condensateur")
plt.plot(t*1e3,e(t),label="$e(t)$")
plt.plot(t*1e3,s,label="$s(t)$")
plt.xlabel("Temps (ms)")
plt.ylabel("Tension (V)")
plt.legend()
plt.show()