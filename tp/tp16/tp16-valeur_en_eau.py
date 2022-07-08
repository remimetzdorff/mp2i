#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 10:29:39 2022
Mesure de la valeur en eau du calorimètre par la méthode des mélanges
@author: remimetzdorff
"""

import numpy as np

#########################
# MESURES ET IMPRÉCISIONS
#########################
# {eau1 + calorimètre}
T1       = 13.75   # température initiale du système {eau1 + calorimètre} en ... 
delta_T1 = 0.1     # imprecision du la température T1 en ...
m1       = 0.31052 # masse d'eau1 en kilogrammes
delta_m1 = 0.00001 # imprécision sur la masse m1 en kg
# {eau2}
T2       = 63.00   # température initiale du système {eau2} en ... 
delta_T2 = 0.1     # imprecision du la température T2 en ...
m2       = 0.25565 # masse d'eau2 en kilogrammes
delta_m2 = 0.00001 # imprécision sur la masse m2 en kg
# température finale
Tf       = 34     # température finale du mélange
delta_Tf = 1      # imprecision du la température Tf en ...

def valeur_en_eau(m1,T1,m2,T2,Tf):
    return - m1 - m2 * (Tf-T2) / (Tf-T1)

#########################
# SIMULATION DE N MESURES
#########################
N = 10000
m1_sim = m1 + np.random.uniform(-delta_m1,delta_m1,N)
T1_sim = T1 + np.random.uniform(-delta_T1,delta_T1,N)
m2_sim = m2 + np.random.uniform(-delta_m2,delta_m2,N)
T2_sim = T2 + np.random.uniform(-delta_T2,delta_T2,N)
Tf_sim = Tf + np.random.uniform(-delta_Tf,delta_Tf,N)
mu_sim = valeur_en_eau(m1_sim, T1_sim, m2_sim, T2_sim, Tf_sim)

val_mu = valeur_en_eau(m1, T1, m2, T2, Tf)
std_mu = np.std(mu_sim)

#######################
# AFFICHAGE DU RÉSULTAT
#######################
print("valeur en eau     : mu    = " + str(val_mu) + " kg")
print("incertitude-type  : u(mu) = " + str(std_mu) + " kg")