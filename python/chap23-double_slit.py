#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 13:27:07 2022
Double-slit experiment
@author: remimetzdorff
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
plt.style.use('dark_background')
from matplotlib.widgets import Slider, Button

fps = 25 # nombre d'images par seconde (pour l'animation)

N = 50000

def fentes_dYoung(x,d=5,l=1):
    return np.sinc(l*x) ** 2 * np.cos(np.pi * d * x) ** 2

x = np.linspace(-1,1,1000)
p = fentes_dYoung(x)
p /= np.sum(p)

photon = []
for i in range(N):
    x_pos = np.random.choice(x,p=p)
    y_pos = np.random.uniform(0,1)
    photon.append([x_pos, y_pos])
photon = np.array(photon)

x_pos = photon[:,0]
y_pos = photon[:,1]

if True:
    plt.figure()
    sps = (3,1)
    ax1 = plt.subplot2grid(sps, (0,0), rowspan=2)
    ax2 = plt.subplot2grid(sps, (2,0), rowspan=1)
    
    ax1.plot(x_pos, y_pos, ".", color="white", markersize=1)
    ax1.set_xlim(-1,1)
    ax1.set_ylim(0,1)
    ax1.set_xticks([])
    ax1.set_yticks([])
    
    ax2.hist(x_pos, bins=500, color="white")
    ax2.set_xlim(-1,1)
    ax2.set_xticks([])
    ax2.set_yticks([])
    ax2.set_ylabel("Counts")
    #ax2.plot(x, p*10*N)

if True:
    n = 1
    # ANIMATION
    fig = plt.figure()
    sps = (3,1)
    ax1 = plt.subplot2grid(sps, (0,0), rowspan=2)
    ax1.set_xlim(-1,1)
    ax1.set_ylim(0,1)
    ax1.set_xticks([])
    ax1.set_yticks([])
    
    axn = plt.axes([0.25, 0.1, 0.65, 0.03])
    n_slider = Slider(ax=axn,
                      label='Photons',
                      valmin=0,
                      valmax=100,
                      valinit=1,
                      valstep=1)
    
    screen, = ax1.plot([], [], ".", color="white", markersize=1)
    
    x_pos, y_pos = [], []
    def animate(i):
        n = int(n_slider.val)
        for k in range(n):
            x_pos.append(np.random.choice(x,p=p))
            y_pos.append(np.random.uniform(0,1))
        screen.set_data(x_pos, y_pos)
        return 
    
    ani = animation.FuncAnimation(fig, animate, frames=N, interval=1e3/fps)
    plt.show()


