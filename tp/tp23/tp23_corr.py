#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 08:28:14 2022
TP23
@author: remimetzdorff
"""

import numpy as np
import matplotlib.pyplot as plt

# Lecture du fichier de données
# ATTENTION : lors de l'export des données depuis Phyphox
#   - le fichier doit être au format CSV
#   - choisir ; comme séparateur de colonnes
#   - choisir . comme séparateur décimal
# => cocher CSV (Semicolon,decimal point)

data = np.genfromtxt('data2.csv', delimiter=';')
t = data[1:,0]
omegax = data[1:,1]
omegay = data[1:,2]
omegaz = data[1:,3]

def integrate(t, omega, theta0=0):
    """
    Intègre numériquement omega(t) pour obtenir theta(t)
    avec la méthode d'Euler
    params: tableau des temps t
            tableau des vitesses angulaires omega
            theta0 : CI
    return: angle theta
    """
    theta = np.zeros(len(t))
    theta[0] = theta0
    for k in range(len(t)-1):
        dt = t[k+1] - t[k]
        theta[k+1] = theta[k] + (omega[k]+omega[k+1]) * dt /2
    return theta

def highpass(t, e):
    s = np.zeros(len(t))
    s[0] = e[0]
    omega0 = 2*np.pi * .2
    for k in range(len(t)-1):
        dt = t[k+1] - t[k]
        s[k+1] = (1 - dt * omega0)*s[k] + e[k+1] - e[k]
    return s
    
omegax = highpass(t, omegax)
omegay = highpass(t, omegay)
omegaz = highpass(t, omegaz)

############################
# REPRÉSENTATIONS GRAPHIQUES
############################
plt.figure(1)
plt.plot(t, omegax, label="$\omega_x$")
plt.plot(t, omegay, label="$\omega_y$")
plt.plot(t, omegaz, label="$\omega_z$")
plt.xlabel("Temps (s)")
plt.ylabel("Vitesse angulaire (rad/s)")
plt.legend(loc="upper right")
plt.grid()

plt.figure(2)
thetax = integrate(t, omegax, theta0=0)
thetay = integrate(t, omegay, theta0=0)
thetaz = integrate(t, omegaz, theta0=0)#-.285)

plt.plot(t, thetax, label="$\\theta_x$")
plt.plot(t, thetay, label="$\\theta_y$")
plt.plot(t, thetaz, label="$\\theta_z$")
plt.xlabel("Temps (s)")
plt.ylabel("Position angulaire (rad)")
plt.legend(loc="upper right")
plt.grid()

omega = np.sqrt(omegax**2 + omegay**2 + omegaz**2)
theta = np.sqrt(thetax**2 + thetay**2 + thetaz**2)
Ec = omega**2 / 41.2
Ep = (1 - np.cos(theta))

plt.figure(3)
plt.plot(t, Ec, label="${\cal E}_c$")
plt.plot(t, Ep, label="${\cal E}_p$")
plt.plot(t, Ec+Ep, label="${\cal E}_m$")
plt.xlabel("Temps (s)")
plt.ylabel("Énergie (u.a.)")
plt.legend(loc="upper right")
#plt.xlim(40,50)
plt.grid()