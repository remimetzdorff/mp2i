#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 08:50:50 2022
Chapitre 18
@author: remimetzdorff
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

n = 3
f = .25
fps = 30
t = np.linspace(0,1/f, int(1/f * fps))

def B(t, phi, a=1):
    omega = 2*np.pi*f
    return a * np.cos(omega*t + phi)

fig, ax = plt.subplots(1)

fields = []
for i in range(n):
    fields.append(ax.quiver(0, 0, 0, 0, color="C"+str(i), alpha=.5, width=.01, angles='xy', scale_units='xy', scale=1.5))
field_rot = ax.quiver(0, 0, 0, 0, alpha=1, width=.01, angles='xy', scale_units='xy', scale=1.5)

ax.set_xlim(-1,1)
ax.set_ylim(-1,1)
ax.set_aspect("equal")
plt.axis("off")

scale=1
if n>1:
    scale = 2/n
def animate(i):
    Bxtot, Bytot = 0, 0
    for k, field in enumerate(fields):
        alpha = k*np.pi/n
        phi = -k*np.pi/n
        Bx = B(t[i], phi, a=scale) * np.cos(alpha)
        By = B(t[i], phi, a=scale) * np.sin(alpha)
        field.set_UVC(Bx,By)
        Bxtot += Bx
        Bytot += By
    field_rot.set_UVC(Bxtot,Bytot)
    return

ani = animation.FuncAnimation(fig, animate, frames=len(t), interval=1e3/fps)
plt.show()