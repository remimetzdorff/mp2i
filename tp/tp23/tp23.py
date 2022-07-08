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

data = np.genfromtxt('data.csv', delimiter=';')
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
        theta[k+1] = theta[k] + omega[k] * dt
    return theta

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
plt.plot(t, integrate(t, omegax, theta0=0), label="$\\theta_x$")
plt.plot(t, integrate(t, omegay, theta0=0), label="$\\theta_y$")
plt.plot(t, integrate(t, omegaz, theta0=0), label="$\\theta_z$")
plt.xlabel("Temps (s)")
plt.ylabel("Position angulaire (rad)")
plt.legend(loc="upper right")
plt.grid()

plt.show()