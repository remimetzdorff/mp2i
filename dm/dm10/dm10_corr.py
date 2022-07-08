#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 12:14:17 2022
DM10
@author: remimetzdorff
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

alpha = .5

def f(V,t):
    """ Fonction associée aux équations différentielles"""
    r, dr, theta = V[0], V[1], V[2]
    ddr    = -alpha/8 + 1/4/r**3
    dtheta = 1 / r**2
    return [dr, ddr, dtheta]

######################
# RÉSOLUTION NUMÉRIQUE
######################
t = np.linspace(0,300,10000) # instants t
V0 = [1,0,0]                 # CI

V = odeint(f,V0,t)           # intégration numérique
r, theta = V[:,0], V[:,2]    # récupération des paramètres r et theta
x = r * np.cos(theta)        # calcul de l'abscisse x
y = r * np.sin(theta)        # calcul de l'ordonnée y

##########################
# REPRÉSENTATION GRAPHIQUE
##########################
plt.figure(1)    # r(t)
plt.title("Évolution du rayon $r^*$")
plt.plot(t, r)
plt.xlabel("$t^*$")
plt.ylabel("$r^*$")
plt.xlim(0, 100)
plt.grid()

plt.figure(2)    # theta(t)
plt.title("Évolution de l'angle $\\theta^*$")
plt.plot(t, theta)
plt.xlabel("$t^*$")
plt.ylabel("$\\theta^*$")
plt.xlim(0, 100)
plt.ylim(-5,40)
plt.grid()

fig = plt.figure(3)    # y(x)
plt.title("Trajectoire")
plt.plot(x, y)
plt.xlabel("$x^*$")
plt.ylabel("$y^*$")
plt.grid()
fig.axes[0].set_aspect("equal") # même échelle sur les deux axes

plt.show()