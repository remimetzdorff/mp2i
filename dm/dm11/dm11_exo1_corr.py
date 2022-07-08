#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 09:41:18 2022
DM11 - Correction
@author: remimetzdorff
"""

import numpy as np
import matplotlib.pyplot as plt

print("QUESTION 5")

l = np.array([0.520, 0.979, 1.516, 2.035, 2.461, 3.034])
T = np.array([14.5, 19.8, 24.7, 28.7, 31.3, 35.0]) / 10
delta_l  = 5e-3    # imprecision sur l
delta_T = 0.2 / 10 # imprecision sur T

# valeur de g : ajustement linéaire des données expérimentales
x = T**2           # abscisse pour l'ajustement linéaire
y = 4*np.pi**2 * l # ordonnée pour l'ajustement linéaire
g, offset = np.polyfit(x, y, 1)

# incertitude : simulation Monte-Carlo
a_sim = []
for k in range(10000):
    T_sim = T + np.random.uniform(-delta_T, delta_T, len(T))
    l_sim = l + np.random.uniform(-delta_l, delta_l, len(l))
    x_sim = T_sim**2
    y_sim = 4*np.pi**2 * l_sim
    a, b = np.polyfit(x_sim,y_sim,1)
    a_sim.append(a)
    
print("g =", g, "+/-", np.std(a_sim, ddof=1), "m.s^-2")

# Représentation graphique
plt.figure(1)
plt.plot(x, y, "o", label="données")
plt.plot(x, g*x + offset, label="ajustement linéaire")
plt.xlabel("$T^2\ (\\rm{s^2})$")
plt.ylabel("$4\pi^2 l$ (m)")
plt.legend()
plt.show()

print("QUESTION 13")

d, delta_d           = 1, 5e-3 * np.sqrt(3)
M, delta_M           = 30, .01 * np.sqrt(3)
a, delta_a           = 10e-2, .2e-2 * np.sqrt(3)
theta0, delta_theta0 = 1.3e-3, .1e-3 * np.sqrt(3)
Tc, delta_Tc         = 510, 10 * np.sqrt(3)

def G(d,a,theta0,M,T):
    return 4*np.pi**2 * d * a**2 * theta0 / M / T**2

d_sim = d + np.random.uniform(-delta_d, delta_d, 10000)
M_sim = M + np.random.uniform(-delta_M, delta_M, 10000)
a_sim = a + np.random.uniform(-delta_a, delta_a, 10000)
theta0_sim = theta0 + np.random.uniform(-delta_theta0, delta_theta0, 10000) 
Tc_sim = Tc + np.random.uniform(-delta_Tc, delta_Tc, 10000)

val_G = G(d,a,theta0,M,Tc)
G_sim = G(d_sim,a_sim,theta0_sim,M_sim,Tc_sim)
uG    = np.std(G_sim, ddof=1)
print("G =", val_G, "+/-", uG, "m^3.kg^-1.s^-2")

print("QUESTION 13 bis")

def incertitude(f, params, uparams, n=10000):
    """
    Calcule l'incertitude-type sur une grandeur
    calculée avec la fonction f
    à partir des grandeurs de la liste params
    auxquelles sont associées les incertitudes-type de la liste uparams
    """
    params_sim = []
    for param, uparam in zip(params, uparams):
        deltaparam = uparam*np.sqrt(3)
        params_sim.append(param + np.random.uniform(-deltaparam,
                                                    deltaparam, n))
    return np.std(f(*params_sim), ddof=1)

d, ud           = 1, 5e-3
M, uM           = 30, .01
a, ua           = 10e-2, .2e-2
theta0, utheta0 = 1.3e-3, .1e-3
Tc, uTc         = 510, 10
params  = [d,a,theta0,M,Tc]
uparams = [ud,ua,utheta0,uM,uTc]
print("G =", G(d,a,theta0,M,Tc), "+/-", incertitude(G,params,uparams), "m^3.kg^-1.s^-2")

print("QUESTION 13 ter")

def incertitude_normal(f, params, uparams, n=10000):
    params_sim = []
    for param, uparam in zip(params, uparams):
        params_sim.append(np.random.normal(param, uparam, n))
    return np.std(f(*params_sim), ddof=1)

print("G =", G(d,a,theta0,M,Tc), "+/-", incertitude_normal(G,params,uparams), "m^3.kg^-1.s^-2")

print("QUESTION 19")

from scipy.optimize import bisect

g, ug = 9.81, .07
h     = 405e3
Ts    = 92*60 + 40

def f(RT):
    return 4*np.pi**2 * (RT + h)**3 - g * Ts**2 * RT**2

print("RT =", bisect(f, 6e6, 7e6), "m (num)")
print("RT =", g*Ts**2/4/np.pi**2 - 3*h, "m (DL)")














