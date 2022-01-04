#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np

#########################
# MESURES ET IMPRÉCISIONS
#########################
# À COMPLÉTER
d             = 1      # pas du réseau en mètres
u_d           = 1      # incertitude-type sur le pas du réseau
alpha_d       = 1      # angle alpha_d (ordre -1) en DEGRÉS
delta_alpha_d = 1      # imprecision sur la mesure de alpha_d
alpha_g       = 1      # angle alpha_g (ordre -1) en DEGRÉS
delta_alpha_g = 1      # imprecision sur la mesure de alpha_g

####################################################
# FORMULE PERMETTANT LE CALCUL DE LA LONGUEUR D'ONDE
####################################################
def longueur_d_onde(alpha_d, alpha_g, d):
    """
    Calcule la longueur d'onde d'un rayonnement en fonction des mesures de
    alpha_d et alpha_g réalisées sur le goniomètre et du pas du réseau utilisé
    """
    Dm_deg = np.abs(alpha_d-alpha_g) / 2 # Déviation minimale en DEGRÉS
    Dm_rad = 0 # Déviation minimale en RADIANS (À COMPLÉTER)
    wl     = 0 # longueur d'onde en mètres (À COMPLÉTER)
    return wl

#######################################
# ESTIMATION DE L'INCERTITUDE DE TYPE B
#######################################
N = 10000
alpha_d_sim = alpha_d + np.random.uniform(-delta_alpha_d,delta_alpha_d,N)
alpha_g_sim = alpha_g + np.random.uniform(-delta_alpha_g,delta_alpha_g,N)
d_sim       = np.random.normal(d, u_d, N)
wl_sim      = longueur_d_onde(alpha_d_sim, alpha_g_sim, d_sim)

print("Estimation de type de B :")
print("lambda    = {:.4e} m".format(np.mean(wl_sim)))
print("u(lambda) = {:.4e} m".format(np.std(wl_sim,ddof=1)))