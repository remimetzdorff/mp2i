#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy.integrate import quad

from tp11_fonctions import euler_deuxieme_ordre

############
# PARAMÈTRES
############
g = 9.81     # accélération de la pesanteur
l = 1        # longueur du pendule
m = 1        # masse 

###################################################
# FONCTIONS ASSOCIÉES AUX ÉQUATIONS DIFFÉRENTIELLES
###################################################
def oh(V,t):
    """
    Fonction associée à un oscillateur harmonique de pulsation propre omega0
    """
    x, y = V
    dx = y
    dy = -g/l * x
    dV = [dx, dy]
    return dV

def pendule(V,t):
    """
    Fonction associée au pendule simple (pulsation propre omega0)
    """
    x, y = V
    dx = y
    dy = -g/l * np.sin(x)
    dV = [dx, dy]
    return dV

##################
# AUTRES FONCTIONS
##################
def borda(theta0):
    T0 = 2*np.pi*np.sqrt(l/g)
    return T0 * (1 + theta0**2/16)

def period_int(theta0):
    """
    Calcul numérique de la valeur de la période, pour une amplitude theta0
    theta0 doit être une valeur unique"""
    def period(x):
        return -1 / np.sqrt(2 * (np.cos(x) - np.cos(theta0)))
    return 4 * quad(period, theta0, 0)[0] / np.sqrt(g/l)

######################
# SIMULATION NUMÉRIQUE
######################
duree  = 20     # duree de la simulation
dt     = .01    # intervalle de temps entre deux instants successifs
t = np.linspace(0, duree, int(duree/dt))

V0     = [np.pi,0.1]  # conditions initiales

V = odeint(oh, V0, t)
theta_oh = V[:,0]
omega_oh = V[:,1]

V = odeint(pendule, V0, t)
theta_pendule = V[:,0]

##########################
# REPRÉSENTATION GRAPHIQUE
##########################
plt.figure(1)
plt.plot(t, theta_oh)
plt.plot(t, theta_pendule)

plt.title("Évolution temporelle de l'angle $\\theta$")
plt.xlabel("Temps (s)")
plt.ylabel("Angle $\\theta$ (rad)")

plt.figure(2)
theta0 = np.linspace(0.01,np.pi/3)
plt.plot(theta0, borda(theta0))

period_integral = []
for theta in theta0:
    period_integral.append(period_int(theta))
plt.plot(theta0, period_integral)
