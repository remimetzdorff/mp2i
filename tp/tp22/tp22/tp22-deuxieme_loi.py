#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 16:36:46 2022
TP22 - Astronomie (partie 1)
@author: remimetzdorff
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("data/earth.txt", skiprows=18, max_rows=1000)
t          = data[:,0] - data[0,0]
x, y, z    = data[:,1], data[:,2], data[:,3]
vx, vy, vz = data[:,7], data[:,8], data[:,9]

# REPRÉSENTATIONS GRAPHIQUES
fig = plt.figure(1)
plt.title("Trajectoire")
plt.xlabel("À compléter")
plt.ylabel("À compléter")
plt.scatter(0, 0)
plt.plot(x, y)
fig.axes[0].set_aspect("equal") # même échelle sur les deux axes
plt.show()