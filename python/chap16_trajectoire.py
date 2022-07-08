#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 11:19:25 2022
chap16 force centrale newtonienne, Cardini2021 p570
@author: remimetzdorff
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import matplotlib.animation as animation

alpha = 1 # Em/E0

def Epeff(r):
    return 1/r**2 - 2/r

def f(V, t):
    r, dr = V[0], V[1]
    ddr    = 1/r**3 - 1/r**2
    dtheta = 1 / r**2
    return [dr, ddr, dtheta]

######################
# RÉSOLUTION NUMÉRIQUE
######################
if alpha == 0:
    r0 = 1/2
    r1, r2 = 1/2, 1/2
else:
    r0 = (-1 + np.sqrt(1+alpha)) / alpha
    r1 = (-1 + np.sqrt(1+alpha)) / alpha
    r2 = (-1 - np.sqrt(1+alpha)) / alpha

if alpha < 0:
    a = (r1 + r2) / 2
    T = 2 * np.pi * a**(3/2)
    t  = np.linspace(0,T,250)
else:
    t  = np.linspace(0,20,250)
V0 = [r0, 0, 0]

V = odeint(f, V0, t)
r = V[:,0]
theta = V[:,2]
x = r * np.cos(theta)
y = r * np.sin(theta)

############################
# REPRÉSENTATIONS GRAPHIQUES
############################
fig = plt.figure(1, figsize=(10,4))
plt.clf()
sps = (1,2)
ax1 = plt.subplot2grid(sps, (0,0))
ax2 = plt.subplot2grid(sps, (0,1))

r_plot = np.linspace(1e-1,10,1000)
ax1.plot(r_plot, Epeff(r_plot), "C3", label="${\cal E}_{\\rm{p,eff}}$")
ax1.hlines(0, 0, 10, "k", alpha=.5, label="${\cal E}_\infty$")
ax1.hlines(alpha, 0, 10, "C0", label="${\cal E}_{\\rm{m}}$")
ax1.set_xlim(0,10)
ax1.set_ylim(-1.1,2)
ax1.plot([r1, r2], [alpha, alpha], "oC0")
ax1.set_xlabel("$r$")
ax1.set_ylabel("$\cal E$")
ax1.set_title("Énergie potentielle effective")
ax1.legend()

ax2.plot([0], [0], "oC1")
ax2.plot(x, y, "C0")
ax2.plot(x, -y, "C0")
ax2.set_aspect("equal")
ax2.set_xlabel("$x$")
ax2.set_ylabel("$y$")
ax2.set_title("Trajectoire")

plt.tight_layout()
###########
# ANIMATION
###########
Ep_profil,   = ax1.plot([r[0]], [Epeff(r[0])], "oC3")
E_profil,    = ax1.plot([r[0]], [alpha], "ok")
trajectoire, = ax2.plot([x[0]], [y[0]], "ok")

def animate(i):
    trajectoire.set_data([x[i]], y[i])
    Ep_profil.set_data([r[i]], [Epeff(r[i])])
    E_profil.set_data([r[i]], [alpha])
    return 

ani = animation.FuncAnimation(fig, animate, frames=len(x), interval=1e3/25)
plt.show()