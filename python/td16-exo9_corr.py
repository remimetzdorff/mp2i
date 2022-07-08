#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 11:48:54 2022
TD16 exo9 (correction)
@author: remimetzdorff
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import bisect

e = 0.5

# Question 1
def g(u):
    return u - e * np.sin(u)

u = np.linspace(-np.pi, np.pi)
plt.plot(u, g(u))
plt.grid()
plt.xlabel("$u$")
plt.ylabel("$g(u)$")

# Pour t = T/3, on cherche la valeur de u tq g(u) = 2 * pi / 3
plt.plot(u, np.ones(len(u))*2*np.pi/3, "--")
# Graphiquement, on lit u = 2.4

# Question 2
# On peut choisir u+ = 2,3 et u- = 2,5.

# Question 3
a, b = 2.3, 2.5
def f(u):
    return g(u) - 2*np.pi/3
u0 = bisect(f, a, b)
print("Solution de l'équation de Kepler (bisect) :", u0)
# Affiche 2.4234054584740083

# Question 4
precision = 2e-12
while (b-a) > precision:
    c = a + (b-a)/2
    if f(a)*f(c) > 0:
        a = c
    else:
        b = c
print("Solution de l'équation de Kepler (dichotomie) :", c)
# Affiche 2.4234054584740075

print ("Écart entre les deux valeurs :", np.abs(u0 - c))
# Affiche 8.881784197001252e-16
# Les deux méthodes donnent le même résultat
# avec au moins la précision demandée.

plt.show()