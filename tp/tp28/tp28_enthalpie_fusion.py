#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 23:10:04 2022
TP28 Enthalpie massique de fusion de l'eau
@author: remimetzdorff
"""

import numpy as np

def incertitude_type(f, params, dparams, n=10000):
    params_sim = []
    for param, dparam in zip(params, dparams):
        deltaparam = dparam
        params_sim.append(param + np.random.uniform(-deltaparam, deltaparam, n))
    return np.std(f(*params_sim), ddof=1)

cl = 4.18e3 # capacité thermique massique de l'eau liquide (USI)
cs = 2.06e3 # capacité thermique massique de l'eau solide (USI)
Tfus = 273.15 # température de fusion de l'eau (K)

def enthalpie_massique(ml, ms, mu, Tl, Ts, Tf):
    return - (ml + mu) / ms * cl * (Tf - Tl)\
           - cs * (Tfus - Ts) - cl * (Tf - Tfus)

#########################
# MESURES ET INCERTITUDES
#########################
ml  = 0.200       # masse d'eau liquide dans le calorimètre (kg)
dml = 0.001       # incertitude sur ml
ms  = 0.020       # masse d'eau solide ajoutée (kg)
dms = 0.001       # incertitude sur ms
mu  = 0.010       # valeur en eau du calorimètre (kg)
dmu = 0.001       # incertitude sur mu
Tl  = 273.15 + 40 # température de l'eau du calorimètre (K)
dTl = 0.1         # incertitude sur Tl
Ts  = 273.15 - 10 # température de la glace (K)
dTs = 0.1         # incertitude sur Ts
Tf  = 273.15 + 30 # température finale (K)
dTf = 0.1         # incertitude sur Tf

params  = [ml, ms, mu, Tl, Ts, Tf]
dparams = [dml, dms, dmu, dTl, dTs, dTf]

#######################
# AFFICHAGE DU RÉSULTAT 
#######################
h_fus  = enthalpie_massique(*params)
uh_fus = incertitude_type(enthalpie_massique, params, dparams)
print("enthalpie massique de fusion = {:} J.kg^-1".format(h_fus))
print("incertitude-type             = {:} J.kg^-1".format(uh_fus))