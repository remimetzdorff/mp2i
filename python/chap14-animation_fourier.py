#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 14:49:06 2022
Série de Fourier à la 3B1B
@author: remimetzdorff
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

scale  = 1
freq   = .25
omega  = 2 * np.pi * freq
period = 1 / freq
fps = 51
xoffset = -3
N = 21
colormap = plt.cm.plasma
if N == 1:
    colorst = [colormap(x) for x in np.linspace(0, 1, 2)]
    colorst = [colorst[1]]
else:
    colorst = [colormap(x) for x in np.linspace(0, 1, N)**.3]#[::-1]

def test(n):
    return 1 / np.sqrt(n)

def square(n):
    if n % 2 == 0:
        return 0
    else:
        return 1 / n
    
def sawtooth(n):
    return 2 * (-1) ** n / n / np.pi

def triangle(n):
    if n % 2 == 0:
        return 0
    else:
        return 8 * (-1) ** ((n-1)/2) / np.pi ** 2 / n ** 2

param  = np.linspace(0, period, 100)

fig = plt.figure(figsize=(8,4)) # initialise la figure
ax = plt.subplot2grid((1,1), (0,0))
ax.set_ylim(-2,2)
ax.set_xlim(-6,6)
ax.set_aspect("equal")
ax.set_facecolor("k")
ax.set_xticks([])
ax.set_yticks([])

radii, circles = [], []
for n in range(N):
    circle, = ax.plot([],[], "-", color = colorst[n], alpha=.5)
    radius, = ax.plot([],[], "-", color = colorst[n])
    radii.append(radius)
    circles.append(circle)
dot, = ax.plot([], [], "o-", color = colorst[N-1], alpha=.5, lw=.5)
signal, = ax.plot([], [], "-", color = colorst[N-1])
ax.plot([0,0], [-2,2], "-", color = colorst[0])

xsignal, ysignal = [], []

def init():
    for n in range(N):
        radius = radii[n]
        circle = circles[n]
        radius.set_data([],[])
        circle.set_data([],[])
    dot.set_data([],[])
    signal.set_data([],[])
    return radii+circles+[dot, signal]

def animate(i):
    t = i / fps
    x, y = [xoffset], [0]
    for n in range(N):
        radius = radii[n]
        circle = circles[n]
        
        s = scale * square(n+1)
        circle.set_data(x[-1] + s * np.cos(omega * param), y[-1] + s * np.sin(omega * param))
        x.append(x[-1] + s * np.cos((n+1) * omega * t))
        y.append(y[-1] + s * np.sin((n+1) * omega * t))
        radius.set_data([x[-2], x[-1]], [y[-2], y[-1]])
    dot.set_data([x[-1], 0], [y[-1], y[-1]])
    xsignal.append(t)
    ysignal.insert(0, y[-1])
    signal.set_data(xsignal, ysignal)
    return radii+circles+[dot, signal]
 
ani = animation.FuncAnimation(fig, animate, init_func=init,
                              frames=10*int(period*fps),
                              interval= 1e3 / fps,
                              blit=True, repeat=False)
plt.tight_layout()
plt.show()