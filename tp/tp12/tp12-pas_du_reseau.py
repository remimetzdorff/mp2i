#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np

#########################
# MESURES ET IMPRÉCISIONS
#########################
wl            = 1e-9 # longueur d'onde en mètres
alpha_d       = 1      # angle alpha_d (ordre -1) en DEGRÉS
delta_alpha_d = 1      # imprecision sur la mesure de alpha_d
alpha_g       = 1      # angle alpha_g (ordre -1) en DEGRÉS
delta_alpha_g = 1      # imprecision sur la mesure de alpha_g

###############################################
# FORMULE PERMETTANT LE CALCUL DU PAS DU RÉSEAU
###############################################
def pas_du_reseau(alpha_d, alpha_g):
    """
    Calcule le pas d du réseau en fonction des mesures de
    alpha_d et alpha_g réalisées sur le goniomètre
    """
    Dm_deg = np.abs(alpha_d-alpha_g) / 2 # Déviation minimale en DEGRÉS
    Dm_rad = 0 # Déviation minimale en RADIANS (À COMPLÉTER)
    d      = 0 # Pas du réseau en mètres (À COMPLÉTER)
    return d

#######################################
# ESTIMATION DE L'INCERTITUDE DE TYPE B
#######################################
N = 10000
alpha_d_sim = alpha_d + np.random.uniform(-delta_alpha_d,delta_alpha_d,N)
alpha_g_sim = alpha_g + np.random.uniform(-delta_alpha_g,delta_alpha_g,N)
d_sim = pas_du_reseau(alpha_d_sim, alpha_g_sim)

print("Estimation de type de B :")
print("d    = {:.4e} m".format(np.mean(d_sim)))
print("u(d) = {:.4e} m".format(np.std(d_sim,ddof=1)))