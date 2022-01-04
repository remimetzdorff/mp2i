#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 18:12:10 2021
Mouvement d'une particule dans un champ (E,B)
@author: remimetzdorff
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import matplotlib.animation as animation

#############################
# PARAMÈTRES DE LA SIMULATION
#############################
q = 1        # charge adimensionnée
m = 1        # masse adimensionnée
E0 = [0,0,0] # champ électrique adimensionné E = (Ex,Ey,Ez)
B0 = [0,0,1] # champ magnétique adimensionné B = (Bx,By,Bz)

M0 = [0,0,0] # position initiale
V0 = [1,0,1] # vitesse initiale

f = 0       # coefficient de frottement

duration = 20 # durée de la simulation
fps      = 25 # nombre d'images par seconde (pour l'animation)

######################
# RÉSOLUTION NUMÉRIQUE
######################
def champ_EB(V,t):
    x, y, z, vx, vy, vz = V
    Ex, Ey, Ez = E0
    Bx, By, Bz = B0
    ax = q/m * (Ex + vy*Bz - vz*By) - f * np.abs(vx) * vx
    ay = q/m * (Ey + vz*Bx - vx*Bz) - f * np.abs(vy) * vy
    az = q/m * (Ez + vx*By - vy*Bx) - f * np.abs(vz) * vz
    dV = (vx,vy,vz,ax,ay,az)
    return dV

t = np.linspace(0,duration,duration*fps*1)
V = odeint(champ_EB, M0+V0, t)
x = V[:,0]
y = V[:,1]
z = V[:,2]

############################
# REPRÉSENTATIONS GRAPHIQUES
############################
fig = plt.figure(figsize=(8,8))
sps = (2,2)
ax1 = plt.subplot2grid(sps,(0,0)) # trajectoire 2D
ax3 = plt.subplot2grid(sps,(1,0)) # trajectoire 2D
ax4 = plt.subplot2grid(sps,(1,1)) # trajectoire 2D
ax2 = plt.subplot2grid(sps,(0,1),projection="3d") # trajectoire 3D

scalex = (max(1,max(abs(x))))
scaley = (max(1,max(abs(y))))
scalez = (max(1,max(abs(z))))
scale  = max(scalex, scaley,scalez)

ax1.plot(x,y,"k")
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.set_aspect("equal")
ax1.set_xlim(-scale,scale)
ax1.set_ylim(-scale,scale)
ax1.set_title("Mouvement dans le plan (Oxy)")

ax3.plot(y,z,"k")
ax3.set_xlabel("y")
ax3.set_ylabel("z")
ax3.set_aspect("equal")
ax3.set_xlim(-scale,scale)
ax3.set_ylim(-scale,scale)
ax3.set_title("Mouvement dans le plan (Oyz)")

ax4.plot(z,x,"k")
ax4.set_xlabel("z")
ax4.set_ylabel("x")
ax4.set_aspect("equal")
ax4.set_xlim(-scale,scale)
ax4.set_ylim(-scale,scale)
ax4.set_title("Mouvement dans le plan (Ozx)")

ax2.plot(x,y,z,color="k")
ax2.quiver([0],[0],[0],[V0[0]],[V0[1]],[V0[2]],color="C0",length=scale/3,normalize=True)
ax2.quiver([0],[0],[0],[E0[0]],[E0[1]],[E0[2]],color="C1",length=scale/3,normalize=True)
ax2.quiver([0],[0],[0],[B0[0]],[B0[1]],[B0[2]],color="C2",length=scale/3,normalize=True)
ax2.set_xlim(-scale,scale)
ax2.set_ylim(-scale,scale)
ax2.set_zlim(-scale,scale)
ax2.set_xlabel("x")
ax2.set_ylabel("y")
ax2.set_zlabel("z")
ax2.set_title("vitesse initiale (bleu)\nchamp E (orange) et champ B (vert)")

###########
# ANIMATION
###########
particule_2dx,  = ax1.plot([], [], "ok")
particule_2dy,  = ax3.plot([], [], "ok")
particule_2dz,  = ax4.plot([], [], "ok")
particule_3d,  = ax2.plot([], [], [], "ok")

def animate(i):
    particule_2dx.set_data([x[i]], [y[i]])
    particule_2dy.set_data([y[i]], [z[i]])
    particule_2dz.set_data([z[i]], [x[i]])
    particule_3d.set_data([x[i]], [y[i]])
    particule_3d.set_3d_properties([z[i]])
    return

ani = animation.FuncAnimation(fig, animate, frames=len(x), interval=1e3/fps)
plt.tight_layout()
plt.show()