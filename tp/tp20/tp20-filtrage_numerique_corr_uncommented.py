#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 18:04:43 2022
TP20 - Filtrage numérique (correction vs sans commentaire
                           pour correction LaTeX)
@author: remimetzdorff
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# CONSTANTES
U0 = 10   # amplitude du signal u(t) en volts
f0 = 50   # fréquence du signal u(t) en hertz
Vs = 0.6  # tension de seuil des diodes en volts
fe = 2*f0 # fréquence du signal e(t) en hertz

cn   = [10.4242, 4.1528, 0.7588, 0.2759] # coefficients cn en volts
phin = [      0,  np.pi,  np.pi,  np.pi] # coefficients phin en radians

def u(t):
    return U0 * np.sin(2*np.pi*f0 * t)

def e(t):
    output = np.abs(u(t)) - 2*Vs
    if hasattr(t, "__len__"):
        for i in range(len(output)):
            output[i] = max(output[i],0)
    else:
        output = max(output,0)
    return output

def e3(t):
    output = cn[0]/2
    for n in range(1,len(cn)):
        output += cn[n] * np.cos(2*np.pi*n*fe * t + phin[n])
    return output

def G1(f, fc):
    return 1 / np.sqrt(1 + (f/fc)**2)

def phi1(f, fc):
    return -np.arctan(f/fc)

def s1(t, fc):
    output = cn[0]/2 * G1(0,fc)
    for n in range(1,len(cn)):
        coefn  = G1(n*fe,fc) * cn[n]
        phasen = phin[n] + phi1(n*fe,fc)
        output += coefn * np.cos(2*np.pi*n*fe * t + phasen)
    return output

def Omega1(fc):
    S = s1(np.linspace(0, 1/fe,10000), fc)
    Seff = np.sqrt(np.mean(S**2))
    Smoy = np.mean(S)
    return Seff/Smoy - 1

def Gp(f, fc, p):
    return 1 / np.sqrt(1 + (f/fc)**2)**p

def phip(f, fc, p):
    return -np.arctan(f/fc) * p

def sp(t, fc, p):
    output = cn[0]/2 * Gp(0,fc,p)
    for n in range(1,len(cn)):
        coefn  = Gp(n*fe,fc,p) * cn[n]
        phasen = phin[n] + phip(n*fe,fc,p)
        output += coefn * np.cos(2*np.pi*n*fe * t + phasen)
    return output

def Omegap(fc, p):
    t = np.linspace(0, 1/fe,10000)
    S = sp(t, fc, p)
    Seff = np.sqrt(np.mean(S**2))
    Smoy = np.mean(S)
    return Seff/Smoy - 1

def s1odeint(t, fc):
    def f(V,t):
        return  (e(t) - V[0]) * 2*np.pi*fc
    return odeint(f, [e(0)], t)[:,0]

def s1euler(t, fc):
    dt     = t[1] - t[0]
    omc    = 2*np.pi*fc
    output = np.zeros(len(t))
    output[0] = e(0)
    for k in range(len(t)-1):
        output[k+1] = output[k] + dt * omc * (e(t[k]) - output[k])
    return output

############################
# REPRÉSENTATIONS GRAPHIQUES
############################
plt.figure(1) # Représentations temporelles des signaux
plt.clf()
fc = 100
t = np.linspace(0,2/f0, 1000)
plt.plot(t, u(t), label="$u(t)$", alpha=.5)
plt.plot(t, e(t), label="$e(t)$")
plt.plot(t, e3(t), label="$e3(t)$")
plt.plot(t, s1(t, fc), label="$s1(t)$")
plt.plot(t, s1odeint(t, fc), label="$s1odeint(t)$")
plt.plot(t, s1euler(t, fc), label="$s1euler(t)$")
plt.plot(t, sp(t, fc, 5), label="$sp(t)$")
plt.title("Évolution temporelle des différents signaux")
plt.xlabel("Temps (s)")
plt.ylabel("Signal (V)")
plt.legend()
plt.grid(which="both")

plt.figure(2) # Effet de la fréquence de coupure
plt.clf()
fcs = np.logspace(0,4)
plt.loglog(fcs, [Omega1(fc) for fc in fcs])
plt.title("Taux d'ondulation à la sortie d'un PB d'ordre 1")
plt.xlabel("Fréquence de coupure du filtre (Hz)")
plt.ylabel("Taux d'ondulation $\Omega$")
plt.grid(which="both")

plt.figure(3) # Effet de l'ordre du filtre
plt.clf()
n = range(1,20)
ond = [Omegap(100, p) for p in n]
plt.semilogy(n, ond, "o", label="$f_c$ = {:.1e} Hz".format(fc))
plt.title("Taux d'ondulation à la sortie d'un PB d'ordre p")
plt.xlabel("Ordre $p$ du filtre")
plt.ylabel("Taux d'ondulation $\Omega$")
plt.grid(which="both")
plt.legend()

plt.figure(4) # Diagramme de Bode
plt.clf()
fc = 100
f = np.logspace(0,5,1000)
for p in range(1,6):
    GdB = 20 * np.log10(Gp(f, fc, p))
    plt.semilogx(f, GdB, label="p = {:.0f}".format(p))
plt.ylim(-120,5)
plt.title("Diagramme de Bode en amplitude, fc = {:.0f} Hz".format(fc))
plt.xlabel("Fréquence (Hz)")
plt.ylabel("Gain (dB)")
plt.grid(which="both")
plt.legend()

plt.show()