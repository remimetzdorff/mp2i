#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 16:36:46 2022
TP22 - Astronomie (partie 1) Correction
@author: remimetzdorff
"""

import numpy as np
import matplotlib.pyplot as plt

def theta(x, y, z):
    """
    params: coordonnées cartésiennes x, y, z
    return: angle theta des coordonnées cylindriques
    """
    return np.unwrap(np.angle(x+1j*y))

data = np.loadtxt("data_prof/earth.txt",skiprows=18, max_rows=1000)
t          = data[:,0] - data[0,0]
x, y, z    = data[:,1], data[:,2], data[:,3]
vx, vy, vz = data[:,7], data[:,8], data[:,9]

############################
# REPRÉSENTATIONS GRAPHIQUES
############################
fig = plt.figure(1)
plt.scatter(0, 0)
plt.plot(x, y)
fig.axes[0].set_aspect("equal") # même échelle sur les deux axes
plt.show()




#### Tests
C = np.sqrt( (y*vz - z*vy)**2 + (z*vx - x*vz)**2 + (x*vy - y*vx)**2 )
Z = (C - C.mean())/C.std()
plt.figure()
plt.plot(t, Z)
plt.show()