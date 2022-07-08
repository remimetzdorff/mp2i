#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 17:01:06 2022
TP20 - Filtrage numérique
@author: remimetzdorff
"""

import numpy as np
import matplotlib.pyplot as plt

# CONSTANTES
U0 = 10   # amplitude du signal u(t) en volts
f0 = 50   # fréquence du signal u(t) en hertz
Vs = 0.6  # tension de seuil des diodes en volts

cn   = [10.4242, 4.1528, 0.7588, 0.2759] # coefficients cn en volts
phin = [      0,  np.pi,  np.pi,  np.pi] # coefficients phin en radians

def u(t):
    """
    params: temps t en secondes
    returns: tension u(t) à la sortie du transformateur en volts
    """
    return U0 * np.sin(2*np.pi*f0 * t)

def e(t):
    """
    params: temps t en secondes
    returns: tension e(t) à la sortie du pont de Graëtz en volts
    """
    output = np.abs(u(t)) - 2*Vs
    if hasattr(t, "__len__"):
        for i in range(len(output)):
            output[i] = max(output[i],0)
    else:
        output = max(output,0)
    return output

############################
# REPRÉSENTATIONS GRAPHIQUES
############################
plt.figure(1)
plt.clf()
t = np.linspace(0,2/f0, 1000) # instants t en secondes pour les graphes
plt.title("Évolution temporelle des différents signaux")
plt.plot(t, u(t), label="$u(t)$")
plt.plot(t, e(t), label="$e(t)$")
plt.xlabel("Temps (s)")
plt.ylabel("Signal (V)")
plt.legend()
plt.grid(which="both")
plt.show()