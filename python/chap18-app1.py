#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 15:23:44 2022
Carte de champ : chap18 app1
@author: remimetzdorff
"""

# Have a look at https://quickfield.com/glossary/magnetic_field_mapping.htm
# and search for vector potential 

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from scipy.integrate import odeint

# mu0 * I / 2 / np.pi / r0 = 1 # avec I = 1A

def mysavefig(filename):
    plt.tight_layout()
    plt.savefig("../images/chap18/"+filename, bbox_inches="tight", dpi=600)
    return

def champB_fil(x,y,x0,y0, r0=.05, I=1):
    r = np.sqrt((x-x0)**2 + (y-y0)**2)
    if r<r0:
        Bt = I * r/r0
    else:
        Bt = I / (r/r0)
    theta = np.angle((x-x0) + 1j*(y-y0))
    Bx = -Bt * np.sin(theta)
    By = Bt * np.cos(theta)
    return Bx, By

def champB(x, y, fils):
    valBx, valBy = 0, 0
    for fil in fils:
        B_component = champB_fil(x, y, fil[0], fil[1], I=fil[2])
        valBx += B_component[0]
        valBy += B_component[1]
    return valBx, valBy

def compute_B(N, width, fils):
    x = np.linspace(-width/2,width/2,N)
    y = np.linspace(-width/2,width/2,N)
    
    B, Bx, By = [], [], []
    #fils = [[1,0,-1]]
    for valy in y:
        B.append([])
        Bx.append([])
        By.append([])
        for valx in x:
            valBx, valBy = 0, 0
            for fil in fils:
                B_component = champB_fil(valx, valy, fil[0], fil[1], I=fil[2])
                valBx += B_component[0]
                valBy += B_component[1]
            B[-1].append(np.sqrt(valBx**2 + valBy**2))
            Bx[-1].append(valBx)
            By[-1].append(valBy)
    return x, y, Bx, By, B

width = 8
fils = [[-1,-.5,1], [1,-.5,-1], [0,.5,-1]]
#fils = [[-1,0,1], [0,0,-1], [1.5,0,2]]
#fils = [[-1,1,1], [-1,0,1], [-1,-1,1], [1,1,-1], [1,0,-1], [1,-1,-1]]
#fils = [[-1,.5,1], [-1,-.5,-1], [1,.5,-1], [1,-.5,1]]

fig = plt.figure(1,figsize=(12,4))
sps = (1,2)
ax1 = plt.subplot2grid(sps, (0,0))
ax2 = plt.subplot2grid(sps, (0,1))
#ax3 = plt.subplot2grid(sps, (0,2))

x, y, Bx, By, B = compute_B(500, width, fils)
ax1.contourf(x, y, B, levels=200, alpha=.5, antialiased=True)

colormap = cm.get_cmap('viridis', 50)
x, y, Bx, By, B = compute_B(30, width, fils)
for j in range(len(y)):
    for i in range(len(x)):
        scale = 1e-3
        #ax2.quiver(x[i], y[j], Bx[j][i]*scale, By[j][i]*scale,
        #           width=.005, angles='xy', scale_units='xy', scale=.0015)
        #ax2.quiver(x[i], y[j], Bx[j][i], By[j][i], width=B[j][i]*1e-2)
        #ax2.quiver(x[i], y[j], Bx[j][i], By[j][i], width=2e-3, alpha=(B[j][i])**(.8))
        xcol = B[j][i]/np.max(B)
        ax1.quiver(x[i], y[j], Bx[j][i]/B[j][i], By[j][i]/B[j][i],
                   width=5e-3, angles='xy', scale_units='xy', scale=5,
                   color=colormap(xcol**.5))

"""
M0 = [0,0]
lineBx, lineBy = [M0[0]], [M0[1]]
step = width/1000
for i in range(10000):
    M = [lineBx[-1], lineBy[-1]]
    Bx, By = champB(M[0], M[1], fils)
    B = np.sqrt(Bx**2 + By**2)
    lineBx.append(lineBx[-1] + step * Bx/B)
    lineBy.append(lineBy[-1] + step * By/B)
    dsquared = (lineBx[-1]-M0[0])**2 + (lineBy[-1]-M0[1])**2
    if np.abs(lineBx[-1]) > width/2:
        break
    elif np.abs(lineBy[-1]) > width/2:
        break
    elif dsquared < step**2:
        break
ax3.plot(lineBx, lineBy)
"""

def plotter(ax):
    for sens in [-1,1]:
        def f(V,t):
            x, y = V
            Bx, By = champB(x, y, fils)
            B = np.sqrt(Bx**2 + By**2)
            dx = sens*Bx/B
            dy = sens*By/B
            return [dx, dy]
        
        M0s = [[k*width/50 - width/2,0] for k in range(51)]
        M0s = [[0,.6], [0,.7], [0,.9], [0, 1.5]]
        M0s += [[-1,-.6], [-1, -.7], [-1, -.9], [-1, -1.5]]
        M0s += [[1,-.6], [1, -.7], [1, -.9], [1, -1.5]]
        M0s += [[-.5,-.25], [1,-.05], [.4,.4], [1.25, .5], [1.5,.75],
                [.05,-1.25], [-2.5,-1], [-3.7,-1.7], [-1,3.6]]
    
        for M0 in M0s:
            t = np.linspace(0,15,1000)
            V = odeint(f, M0, t, rtol=1e-6,atol=1e-6)
            lineBx, lineBy = V[:,0], V[:,1]
            ax.plot(lineBx, lineBy, "C0", lw=1)
    return
#ax3.streamplot(x, y, Bx, By, color="C0", linewidth=1, cmap=plt.cm.inferno,density=2, arrowstyle='->', arrowsize=1.5)
plotter(ax2)

for ax in [ax1, ax2]:
    ax.set_aspect("equal")
    ax.set_xlim(-width/2,width/2)
    ax.set_ylim(-width/2,width/2)
    ax.axis("off")

fig, ax = plt.subplots(1, figsize=(6,4))
plotter(ax)
ax.set_aspect("equal")
ax.set_xlim(-4,4)
ax.set_ylim(-2.75,2.75)
plt.axis("off")

#mysavefig("true_field_line.pdf")









