#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

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
    Fonction associée au pendule linéarisé (oscillateur harmonique)
    """
    x, y = V
    dx = y
    dy = - g/l * x
    dV = [dx, dy]
    return dV

def pendule(V,t):
    """
    Fonction associée au pendule simple
    """
    # À COMPLÉTER
    return

########################
# SIMULATIONS NUMÉRIQUES
########################
duree  = 10      # duree de la simulation
dt     = .01     # intervalle de temps entre deux instants successifs
t = np.linspace(0, duree, int(duree/dt))

V0     = [0.1, 0]  # conditions initiales
V = odeint(oh, V0, t) # intégration numérique de l'équation différentielle
theta_oh = V[:,0]  # valeurs de theta pour l'oscillateur harmonique
omega_oh = V[:,1]  # valeurs de omega pour l'oscillateur harmonique

############################
# REPRÉSENTATIONS GRAPHIQUES
############################
plt.figure(1)
plt.plot(t, theta_oh)
plt.title("Titre")
plt.xlabel("À compléter")
plt.ylabel("À compléter")
plt.show()