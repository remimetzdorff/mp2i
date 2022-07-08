#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 09:03:55 2022
TD17 exo5
@author: remimetzdorff
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint, quad
import matplotlib.animation as animation

# mg = 1
# 3g/l = 1
theta0 = 5 * np.pi / 180 # angle initial
fps = 30

def Rr(theta):
    return 1/2 * (5*np.cos(theta) - 3*np.cos(theta0))

def Rt(theta):
    return -1/4 * np.sin(theta)

def Rx(theta):
    return Rr(theta)*np.cos(theta) - Rt(theta)*np.sin(theta)

def Ry(theta):
    return Rr(theta)*np.sin(theta) + Rt(theta)*np.cos(theta)
    
def chute(V,t):
    theta, dtheta = V
    ddtheta = 1/2 * np.sin(theta)
    return [dtheta, ddtheta]

def temps_chute(theta):
    return 1 / np.sqrt(np.cos(theta0) - np.cos(theta))

tau = quad(temps_chute, theta0, np.pi)[0] # Durée de la chute

t = np.linspace(0,2*tau,int(tau*fps))
V = odeint(chute, [theta0,0], t)
theta = V[:,0]
x = np.cos(theta)
y = np.sin(theta)

fig, ax = plt.subplots(1)
ax.plot([-1.1, 1.1], [0,0], "k") # le sol
tronc, = ax.plot([0,y[0]], [0,x[0]], "maroon", lw=5, solid_capstyle='round', alpha=.5)
plt.fill_between([-4,4], [0,-10], color="k", alpha=0.25)
reac   = ax.quiver(0, 0, 0, 0, color="C0", alpha=1, width=.01, angles='xy', scale_units='xy', scale=.0015)
poids  = ax.quiver(0, 0, 0, 0, color="C2", alpha=1, width=.01, angles='xy', scale_units='xy', scale=.0015)

ax.set_title("Arbre ou pendule ?")
ax.set_xlim(-1.1,1.1)
ax.set_ylim(-1.1,1.6)
ax.set_xticks([])
ax.set_yticks([])
ax.set_aspect("equal")

def animate(i):
    scale = .5e-3
    tronc.set_data([0, y[i]], [0,x[i]])
    reac.set_UVC(Ry(theta[i])*scale, Rx(theta[i])*scale)
    reac.set_offsets((0,0))
    poids.set_UVC(0*scale, -1*scale)
    poids.set_offsets((y[i]/2,x[i]/2))
    return 

ani = animation.FuncAnimation(fig, animate, frames=len(x), interval=1e3/fps)
plt.show()