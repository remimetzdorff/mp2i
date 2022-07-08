#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 20:13:40 2022
Tracé de G et phi pour l'exercice 4 du TD13
@author: remimetzdorff
"""

# REMARQUE : Python sait gérer les complexe !
# On utilise la syntaxe 1j pour écrire le nombre dont le carré vaut -1

import numpy as np
import matplotlib.pyplot as plt

def H(f,f0,Q):
    """
    Fonction de transfert du circuit RLC série.
    La sortie correspond à la tension aux bornes du condensateur.
    Puisque c'est le rapport omega/omega0 qui intervient
    dans l'expression de H, on peut indiféremment utiliser le rapport f/f0.
    args:
        f  : fréquence du générateur
        f0 : fréquence propre du circuit
        Q  : facteur de qualité du circuit
    return:
        H(j*omega) : valeur complexe du rapport uC/e
    """
    return 1 / (1 - (f/f0)**2 + 1j * f/f0/Q)

##########################
# REPRÉSENTATION GRAPHIQUE
##########################
plt.figure()                  # préparation de la figure
sps = (3,1)
ax1 = plt.subplot2grid(sps, (0,0),rowspan=2)
ax2 = plt.subplot2grid(sps, (2,0))

f0 = 1e3                       # fréquence propre du circuit en Hz
for Q in [1/2, 2, 10]:         # tracé des courbes pour les valeurs de Q demandées
    f = np.logspace(2,4, 1000) # fréquences entre 10**2 et 10**4 Hz, en échelle log
    h = H(f,1e3,Q)             # valeurs complexe de la fonction de transfert
    g = np.abs(h)              # module d'un complexe avec np.abs
    phi = np.angle(h)          # argument d'un complexe avec np.angle
    phi *= 180/np.pi           # puis conversion en degrés
    
    ax1.semilogx(f, g, label=Q)# le gain
    ax2.semilogx(f,phi)        # la phase

# Mise en forme
ax1.set_title("Résonance en tension aux bornes du condensateur")
ax1.set_xticklabels([])
ax1.grid(which="both")
ax1.set_ylabel("Gain $G$")
ax1.legend()

ax2.grid(which="both")
ax2.set_xlabel("Fréquence (Hz)")
ax2.set_ylabel("Phase (°)")

plt.show()