#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 17:18:57 2022
Peut-on calculer l'évolution de N particules ?
Ça dépend de la valeur de N...
@author: remimetzdorff
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

n = 1000 # nombre d'itérations
t = np.linspace(0,1,n)

def chute_libre(V,t):
    z, dz = V
    return [dz,-2]

V = odeint(chute_libre, [1,0], t)
z = V[:,0]

plt.plot(np.zeros(len(t)),z, "o")
plt.xlabel("$x$")
plt.ylabel("$z$")
plt.title("Chute libre")

# choisir n pour avoir un temps de calcul propto n (n=1e5)
# %timeit odeint(chute_libre, [1,0], t)
# T = # noter la valeur
# T/n # une itération
# T/n * 3 # passage en trois dimensions
# T/n * 3 * 1e23 # pour tous le système
# à convertir en heures, jours, années, présence humaine (7 Ma), age de la Terre (4,5 Ga), univers (13,8 Ga)
# intervalle de temps à choisir : 1e-7 / 1000