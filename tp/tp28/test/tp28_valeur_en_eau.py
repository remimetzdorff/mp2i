#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 22:57:20 2022
TP28 Valeur en eau du calorimètre
@author: remimetzdorff
"""

import numpy as np

def incertitude_type(f, params, dparams, n=10000):
    params_sim = []
    for param, dparam in zip(params, dparams):
        deltaparam = dparam
        params_sim.append(param + np.random.uniform(-deltaparam, deltaparam, n))
    return np.std(f(*params_sim), ddof=1)

def valeur_en_eau(m1, m2, T1, T2, Tf):
    return - m2 * (Tf - T2) / (Tf - T1) - m1

#########################
# MESURES ET INCERTITUDES
#########################
mb  = 0.1018 
m1  = 0.2037 + 0.2027 - 2*mb       # masse d'eau dans le calorimètre (kg)
dm1 = 0.0005       # incertitude sur m1
m2  = 0.260 - mb       # masse d'eau ajoutée (kg)
dm2 = 0.0005       # incertitude sur m2
T1  = 273.15 + 21.95 # température de l'eau du calorimètre (K)
dT1 = 0.5         # incertitude sur T1
T2  = 273.15 + 72.23 # température de l'eau ajoutée (K)
dT2 = 0.5         # incertitude sur T2
Tf  = 273.15 + 41.9 # température finale (K)
dTf = 0.5         # incertitude sur Tf

params  = [m1, m2, T1, T2, Tf]
dparams = [dm1, dm2, dT1, dT2, dTf]

#######################
# AFFICHAGE DU RÉSULTAT 
#######################
mu  = valeur_en_eau(*params)
umu = incertitude_type(valeur_en_eau, params, dparams)
print("valeur en eau    = {:} kg".format(mu))
print("incertitude-type = {:} kg".format(umu))