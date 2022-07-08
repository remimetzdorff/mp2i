#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 15:12:33 2022
Résonance en intensite (tension aux bornes de la résistance)
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

def de(t):
    # dérivée du signal du GBF
    return -omega * np.sin(omega * t)

def rlc(V,t):
    # fonction associée à l'équation différentielle
    s, ds = V
    dds = - omega0**2 * s + omega0/Q * (de(t) - ds)
    dV = [ds, dds]
    return dV

########################################
# RÉSOLUTION ET REPRÉSENTATION GRAPHIQUE
########################################
t = np.linspace(-10*Q/omega0,5*2*np.pi/omega,1000) # temps t en seconde
V = odeint(rlc, [0,0], t)
s = V[:,0]                   # tension aux bornes de C

plt.title("Résonance en intensité (tension aux bornes de la résistance)")
plt.plot(t,e(t),label="$e(t)$")
plt.plot(t,s,label="$s(t)$")
plt.xlabel("Temps (s)")
plt.ylabel("Tension (V)")
#plt.xlim(0,5*2*np.pi/omega)
plt.legend()
plt.show()