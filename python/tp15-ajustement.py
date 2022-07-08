#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 18:53:03 2022
Ajustement linéaire
@author: remimetzdorff
"""

import numpy as np
import matplotlib.pyplot as plt

# Pour vérifier une loi linéaire y = a*x, on réalise une série de mesures
# de y en faisant varier x. On souhaite déterminer la valeur de a
# et estimer l'incertitude type associée.

#########################
# MESURES ET IMPRÉCISIONS
#########################
x = np.array([5.6, 9.7, 15.3, 20.5, 25.0, 30.5, 34.7, 39.0, 45.0, 50.2, 55.0, 61.0])
delta_x = 0.1
y = np.array([1.8, 3.2,  4.9,  6.5,  8.3,  9.7, 11.0, 12.6, 14.1, 15.9, 17.3, 19.3])
delta_y = 0.5

plt.plot(x,y,"oC0") # sans barre d'erreur
plt.errorbar(x,y, xerr=delta_x, yerr=delta_y, fmt="o", capsize=2, label="Données") # avec barres d'erreur

#####################
# AJUSTEMENT LINÉAIRE
#####################
a, b = np.polyfit(x,y,1)
plt.plot(x, a*x+b, label="Ajustement")

plt.title("Regression linéaire")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()

print("PARAMÈTRES DE L'AJUSTEMENT")
print("Coefficient directeur a    :", a)
print("Ordonnée à l'origine  b    :", b)

##############################################
# ESTIMATION DE L'INCERTITUDE SUR LES PARAMÈTRES DE L'AJUSTEMENT
##############################################
tab_a, tab_b = [], []
for n in range(10000):
    x_sim = x + np.random.uniform(-delta_x,delta_x,len(x))
    y_sim = y + np.random.uniform(-delta_y,delta_y,len(y))
    a_sim, b_sim = np.polyfit(x_sim,y_sim,1)
    tab_a.append(a_sim) # coefficient directeur
    tab_b.append(b_sim) # ordonnée à l'origine

print("INCERTITUDES-TYPES")
print("Coefficient directeur u(a) :", np.std(tab_a,ddof=1))
print("Ordonnée à l'origine  u(b) :", np.std(tab_b,ddof=1))