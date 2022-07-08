#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 20:38:00 2021
Mouvement dans un potentiel similaire au potentiel de Lennard-Jones
@author: remimetzdorff
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import matplotlib.animation as animation

#############################
# PARAMÈTRES DE LA SIMULATION
#############################
E0    = 5     # facteur d'échelle pour le profil d'énergie potentielle
d     = 1     # distance caractéristique
m     = 1     # masse du point matériel

duration = 30  # durée de la simulation
fps      = 25 # nombre d'images par seconde (pour l'animation)
ralenti  = 1
# CONDITIONS INITIALES
deq = 1.26 * d
x0 = deq   # position initiale
v0 = -1   # vitesse initiale

##########
# ÉNERGIES
##########
def energy_potentielle(r):
    return 4 * E0 * ( (d/r)**6 - (d/r)**3 )
def energy_cinetique(v):
    return 0.5 * m * v**2
def energy_mecanique(x,v):
    return energy_cinetique(v) + energy_potentielle(x)

######################
# RÉSOLUTION NUMÉRIQUE
######################
def eqdiff(V,t):
    """Équations différentielles associées au problème"""
    x,v = V
    dx = v
    dv = 4 * E0 * (6 * d**6/x**7 - 3 * d**3/x**4)
    return [dx, dv]

t = np.linspace(0,duration,duration*fps*ralenti)
V = odeint(eqdiff, [x0,v0], t)
x = V[:,0]
v = V[:,1]

############################
# REPRÉSENTATIONS GRAPHIQUES
############################
fig = plt.figure(figsize=(8,8))
sps = (3,1)
ax1 = plt.subplot2grid(sps,(0,0),rowspan=2) # profil d'énergie potentielle
ax2 = plt.subplot2grid(sps,(2,0)) # trajectoire

x_plot = np.linspace(0,5,1000)
ax1.plot(x_plot, energy_potentielle(x_plot), "k")
ax1.plot([0,5],np.ones(2)*energy_mecanique(x0, v0), "--", alpha=.5)
ax1.annotate("${\cal E}_m$", (4.75, .2+energy_mecanique(x0, v0)), color="C0", size=15)
ax1.set_xlim(min(x_plot), max(x_plot))
ax1.set_ylim(-1.1*E0, 5)
ax1.set_xlabel("$x$ (m)")
ax1.set_ylabel("${\cal E}_p$ (J)")
ax1.set_title("Profil d'énergie potentielle")

ax2.plot([0,10],[0,0], "k")
ax2.set_xlim(min(x_plot), max(x_plot))
ax2.set_xlabel("$x$ (m)")
ax2.set_yticks([])
ax2.set_title("Mobile")

plt.tight_layout()

###########
# ANIMATION
###########
Ec_profil,    = ax1.plot([], [], "oC1")
Ep_profil,    = ax1.plot([], [], "ok")
Em_profil,    = ax1.plot([], [], "oC3")
trajectoire,  = ax2.plot([], [], "ok", ms=10)

def animate(i):
    trajectoire.set_data([x[i]], [0])
    ax2.set_title("$x$ = {:.2f} m, $v$ = {:.2f} m/s".format(x[i], v[i]))
    Ep_profil.set_data([x[i]], [energy_potentielle(x[i])])
    ax1.set_title("$E_p$ = {:.2f} J, $E_c$ = {:.2f} J".format(energy_potentielle(x[i]),
                                                              energy_cinetique(v[i])))
    return 

ani = animation.FuncAnimation(fig, animate, frames=len(x), interval=1e3/fps)
plt.show()