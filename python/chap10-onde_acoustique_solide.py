#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 01:22:47 2022
Onde élastique dans un solide
@author: remimetzdorff
"""

#############################################
# MODELE DE PROPAGATION DU SON DANS UN SOLIDE
#############################################

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib import rcParams

#########
# Options
#########
show_labels           = False # légendes de la figure
show_witness_particle = True # particule témoin
fps = 25

######################
# Paramètres de l'onde
######################
f     = 0.5          # fréquence en Hz
omega = 2.*np.pi * f # pulsation de l'onde
scale = 0.03         # amplitude de déplacement en u.a.

######################
# Paramètres du solide
######################
c     = 0.2     # vitesse de propagation en u.a./s
k     = omega/c # vecteur d'onde
nx    = 51      # nombre de particules selon x
ny    = 31      # nombre de particules selon y

##################################
# Position des particules au repos
##################################
x = list(np.linspace(-1,1,nx))
y = list(np.linspace(-0.1,0.1,ny))

newx, newy = [], []
for iy in range(len(y)):
    newx+=x
for i, val in enumerate(newx): # ajout d'un peu d'aléatoire, c'est plus joli
    newx[i] = val + np.random.normal(loc=0, scale=scale/2)
for val in y:
    newy += list(val*np.ones(len(x)))
for i, val in enumerate(newy): # ajout d'un peu d'aléatoire, c'est plus joli
    newy[i] = val + np.random.normal(loc=0, scale=scale/10)
x, y = np.array(newx), np.array(newy)

##########################
# Vibration des particules
##########################
def pos(x, t):
    return x + scale*np.sin(omega*t-k*x)
# Pour représenter la vitesse des particules
X = np.linspace(-1,1, 1000)
def Y(X,t):
    return np.cos(omega*t-k*X)

#########################
# Paramètres de la figure
#########################
fig = plt.figure(figsize=(6,4))
sps = (2,1)
ax1 = plt.subplot2grid(sps, (0,0))
ax2 = plt.subplot2grid(sps, (1,0))
for ax in [ax1, ax2]:
    ax.set_xlim(x.min()+scale,x.max()-scale)
ax1.set_ylim(y.min(),y.max())
ax2.set_ylim(-1.1, 1.1)

if show_labels:
    ax1.set_title("Particules dans le solide")
    ax1.set_xlabel("x (a.u.)")
    ax1.set_ylabel("y (a.u.)")
    ax2.set_title("Onde de vitesse")
    ax2.set_xlabel("x (a.u.)")
    ax2.set_ylabel(r"$v_x$ (a.u.)")
else:
    for ax in [ax1, ax2]:
        ax.set_xticks([])
        ax.set_yticks([])

# Les différentes "courbes"
line1,     = ax1.plot([], [], "oC0", markersize=2) # les particules
line1_dot, = ax1.plot([], [], "oC1", markersize=6) # LA particule
line2,     = ax2.plot([], [], "-C0")               # la vitesse
plt.tight_layout()

###########
# Animation
###########
def init():
    line1.set_data([], [])
    line1_dot.set_data([], [])
    line2.set_data([], [])
    return line1,

def animate(i):
    t=i/fps
    line1.set_data(pos(x,t), y)
    if show_witness_particle:
        line1_dot.set_data([pos(0,t)], [0])
    line2.set_data(X, Y(X,t))
    return line1,

anim = animation.FuncAnimation(fig, animate, frames=int(1/f*fps)+1, interval=1e3/fps, init_func=init)

############
# Sauvegarde
############
save_format = None # None, "mp4" ou "gif"
dpi = 200

# writer
path = "./Documents/Github/enseignements/2020-2021_lycee_suzanne_valadon_limoges/cours/python/son/"
if save_format == "mp4":
    Writer = animation.writers['ffmpeg']
elif save_format == "gif":
    # requiert ImageMagick : brew install imagemagick
    # make sure the full path for ImageMagick is configured
    # to find the path, type in console > which convert
    rcParams['animation.convert_path'] = r"/usr/local/bin/convert"
    Writer = animation.writers['imagemagick']
# sauvegarde
if save_format is None:
    pass
else:
    writer = Writer(fps=fps, metadata=dict(artist='Me'), bitrate=1800)
    anim.save(path+"animation."+save_format, writer=writer, dpi=dpi)
