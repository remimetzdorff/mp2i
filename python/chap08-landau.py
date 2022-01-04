#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 16:14:36 2021
Oscillateur de Landau animé
@author: remimetzdorff
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import matplotlib.animation as animation

#############################
# PARAMÈTRES DE LA SIMULATION
#############################
l0 = 1               # longueur à vide du ressort
l1 = l0*.5          # distance du point d'accroche
k  = 20              # constante de raideur du ressort
m  = 1               # masse du point matériel
a  = 0             # coefficient de frottement (linéaire)

duration = 5        # durée de la simulation
fps      = 25        # nombre d'images par seconde (pour l'animation)

##########
# ÉNERGIES
##########
def length(x):
    return np.sqrt(l1**2+x**2)
def energy_ressort(x):
    return 0.5 * k * (length(x)-l0) ** 2
def energy_cinetique(v):
    return 0.5 * m * v**2
def energy_mecanique(x,v):
    return energy_cinetique(v) + energy_ressort(x)

if l0 > l1:
    xeq = np.sqrt(l0**2 - l1**2) # position d'équilibre
else:
    xeq = 0
vlim = np.sqrt(2/m * energy_ressort(0)) # vitesse limite

# CONDITIONS INITIALES
x0 = xeq
v0 = 2.

######################
# RÉSOLUTION NUMÉRIQUE
######################
def landau(V,t):
    """Équations différentielles associées au problème"""
    x,v = V
    dx = v
    dv = - k / m * x * (1 - l0/length(x)) - a * v
    return [dx, dv]

t = np.linspace(0,duration,duration*fps*1)
V = odeint(landau, [x0,v0], t)
x = V[:,0]
v = V[:,1]

############################
# REPRÉSENTATIONS GRAPHIQUES
############################
fig = plt.figure(figsize=(12,8))
sps = (2,2)
ax1 = plt.subplot2grid(sps,(1,0)) # profil d'énergie potentielle
ax2 = plt.subplot2grid(sps,(0,0)) # animation
ax3 = plt.subplot2grid(sps,(0,1)) # évolution temporelle de x
ax4 = plt.subplot2grid(sps,(1,1)) # évolution temporelle de l'énergie

x_plot = np.linspace(-2*l0,2*l0,1000)
ax1.plot(x, energy_cinetique(v), "C1", alpha=.1)
ax1.plot(x_plot, energy_ressort(x_plot), "C2")
ax1.plot(x, energy_mecanique(x, v), "C3", alpha=.1)
ax1.set_xlim(min(x_plot), max(x_plot))
ax1.set_ylim(min(energy_ressort(x_plot))-1, max(energy_ressort(x_plot)))
ax1.set_title("Profil d'énergie potentielle")
ax1.set_xlabel("Position $x$")
ax1.set_ylabel("Énergie potentielle ${\cal E}_p$")

ax2.plot(x_plot, np.zeros(len(x_plot)), "k")
ax2.set_ylim(-.1, 2*l1)
ax2.set_xlim(min(x_plot), max(x_plot))
ax2.set_title("Oscillateur de Landau")
ax2.set_xlabel("Position $x$")
ax2.set_yticks([])

ax3.plot(t, x)
ax3.set_xlim(min(t), max(t))
ax3.set_ylim(-2,2)
ax3.set_title("Évolution de la position")
ax3.set_xlabel("Temps $t$")
ax3.set_ylabel("Position $x$")

ax4.plot(t, energy_cinetique(v), "C1", label="${\cal E}_c$")
ax4.plot(t, energy_ressort(x), "C2", label="${\cal E}_p$")
ax4.plot(t, energy_mecanique(x, v), "C3", label="${\cal E}_m$")
ax4.set_xlim(min(t), max(t))
ax4.set_ylim(min(-0.1,-.1*energy_mecanique(x0, v0)),max(0.1, 1.1*energy_mecanique(x0, v0)))
ax4.set_title("Évolution des énergies ${\cal E}_c$, ${\cal E}_p$ et ${\cal E}_m$ ")
ax4.set_xlabel("Temps $t$")
ax4.set_ylabel("Énergie $\cal E$")
ax4.legend()

plt.tight_layout()
###########
# ANIMATION
###########
Ec_profil,    = ax1.plot([], [], "oC1")
Ep_profil,    = ax1.plot([], [], "oC2")
Em_profil,    = ax1.plot([], [], "oC3")
oscillateur,  = ax2.plot([], [], "o-k")

def animate(i):
    oscillateur.set_data([0,x[i]], [l1,0])
    Ec_profil.set_data([x[i]], [energy_cinetique(v[i])])
    Ep_profil.set_data([x[i]], [energy_ressort(x[i])])
    Em_profil.set_data([x[i]], [energy_mecanique(x[i], v[i])])
    return oscillateur, 

ani = animation.FuncAnimation(fig, animate, frames=len(x), interval=1e3/fps)
plt.show()