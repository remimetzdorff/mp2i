#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import matplotlib.animation as animation

omega0 = 2*np.pi*.3
duree  = 15
fps    = 25

def oh(V,t):
    return [V[1], -omega0**2*V[0]]

def pendule(V,t):
    return [V[1], -omega0**2*np.sin(V[0])]

t = np.linspace(0, duree, int(duree*fps))
V0     = [3*np.pi/2,0]

V_oh = odeint(oh, V0, t)
theta_oh = V_oh[:,0]
V_pendule = odeint(pendule, V0, t)
theta_pendule = V_pendule[:,0]

fig = plt.figure(figsize=(10,4))
sps = (1,2)
ax1 = plt.subplot2grid(sps,(0,0))
ax2 = plt.subplot2grid(sps,(0,1))
ax1.set_title("Oscillateur harmonique")
ax2.set_title("Pendule")
for ax in [ax1,ax2]:
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(-1.1,1.1)
    ax.set_ylim(-1.1,1.1)
    ax.set_aspect("equal")
    
pendule_oh,     = ax1.plot([], [], "o-C0")
pendule_nonlin, = ax2.plot([], [], "o-C1")

def animate(i):
    x, z = np.sin(theta_oh[i]), -np.cos(theta_oh[i])
    pendule_oh.set_data([0,x], [0,z])
    x, z = np.sin(theta_pendule[i]), -np.cos(theta_pendule[i])
    pendule_nonlin.set_data([0,x], [0,z])
    return pendule_oh, pendule_nonlin

ani = animation.FuncAnimation(fig, animate, frames=len(t), interval=1e3/fps)
plt.show()