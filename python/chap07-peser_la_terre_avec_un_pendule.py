# Ce programme permet de garder une trace de la mesure de la masse de la Terre
# réalisée à partir de la mesure de la période des oscillation d'un pendule simple
# Mesure réalisée le mardi 30/11/21

import numpy as np
import astropy.constants as csts

##########################
# MESURES DE DIX PÉPRIODES
##########################
# Ci-dessous, les données brutes récupérées d'après vos réponses sur https://answergarden.ch/
# 12.75,11.97,13.03,12.57,12.97,12.42,13.58,12.83,12.7,12.68,12.51,12.53,11.78,13.25,16,12.50,10.53,12,78,12.90,14.11,13.32,13.65,13.5,12.02,12,86,13.4,14,14.15,12.31,12.79,1.336,12,75,12.38,1.320,12.78,11.8,12.2,12.88,11.45,12.46,11.31,1.323,12.91,11.49,12.71,12.67,12.76,6.66,11.7,1.34,12.44,12.03,11.84,13.39,12.73,11.88,12.9,
# Dans le tableau ci-dessous, j'ai corrigé les valeurs qui me semblaient aberrantes :
#    quelques uns ont utiliser une "," comme séparateur décimal, à la place d'un "."
#    d'autres ont rentré la période et pas la durée des dix périodes
mesures = np.array([12.75,11.97,13.03,12.57,12.97,12.42,13.58,12.83,12.7,12.68,12.51,12.53,11.78,13.25,16,12.50,10.53,12.78,12.90,14.11,13.32,13.65,13.5,12.02,12.86,13.4,14,14.15,12.31,12.79,13.36,12.75,12.38,13.20,12.78,11.8,12.2,12.88,11.45,12.46,11.31,13.23,12.91,11.49,12.71,12.67,12.76,6.66,11.7,13.4,12.44,12.03,11.84,13.39,12.73,11.88,12.9,])
T = mesures/10 # durée d'une période (s)

l = 0.43 # Mesure de la longueur du pendule en mètres

###############################################################
# ACCÉLÉRATION DE LA PESANTEUR DANS LA 101 DU LYCÉE PAUL VALÉRY
###############################################################
g = 4*(np.pi**2)*l/T**2                # calcul des n valeurs de g
val_g = np.mean(g)                     # on garde la moyenne
ecarttype_exp = np.std(g, ddof=1)      # écart-type expérimental
uA_g = ecarttype_exp / np.sqrt(len(g)) # incertitude-type de type à sur g
print("############# Mesure de g #############")
print("Valeur de g : {:.2f} m/s2".format(val_g))         # mesure
print("Référence   : {:.2f} m/s2".format(csts.g0.value)) # valeur de référence
print("Écart-type expérimental    : {:.2f} m / s2".format(ecarttype_exp))
print("Incertitude-type de type A : {:.2f} m / s2".format(uA_g))
print()

################
# PESER LA TERRE
################
M = 4*np.pi**2*l*csts.R_earth.value**2/csts.G.value/T**2
val_M = np.mean(M)
uA_M  = np.std(M, ddof=1) / np.sqrt(len(M))
print("########## Mesure de M_Terre ##########")
print("Masse de la Terre          : {:.2e} kg".format(val_M))
print("Incertitude-type de type A : {:.2e} kg".format(uA_M))
print("Référence                  : {:.2e}".format(csts.M_earth))

#################################################################
# COMPARAISON DE LA MESURE DE M_Terre AVEC LA VALEUR DE RÉFÉRENCE
#################################################################
# Valeur de référence issue du CODATA 2018
val_M_ref = csts.M_earth.value # valeur de référence via astropy.constants
Z = np.abs(val_M - val_M_ref) / uA_M
print("Z-score : {:.2f}".format(Z))
# Le Z-score est supérieur à 2, la valeur mesurée n'est pas en accord
# avec la valeur de référence. On n'a pas pris en compte l'incertitude
# sur la mesure de T et sur la mesure de l (type B).

#######################
# INCERTITUDE DE TYPE B
#######################
# On estime l'imprécision sur la mesure de l à +/- 0,5 cm
# et celle sur la mesure des 10 périodes à +/- 0,5 s
delta_l       = .5e-2
delta_mesures = .5
delta_T       = delta_mesures/10

# On fait simule un grand nombre de mesures pour avoir estimer
# l'incertitude-type de type B sur M_Terre
l_sim = l + np.random.uniform(-delta_l,+delta_l,10000)
T_sim = np.mean(T) + np.random.uniform(-delta_T,+delta_T,10000)
M_sim = 4*np.pi**2*l_sim*csts.R_earth.value**2/csts.G.value/T_sim**2
val_M_sim = np.mean(M_sim)
uB_M      = np.std(M_sim,ddof=1)
print("Masse de la Terre          : {:.2e} kg".format(val_M_sim))
print("Incertitude-type de type B : {:.2e} kg".format(uB_M))
print()

############
# CONCLUSION
############
u_M = np.sqrt(uA_M**2 + uB_M**2) # Incertitude-type totale
Z   = np.abs(val_M_sim - val_M_ref) / u_M
# Cette fois, le Z-score indique un écart raisonnable entre l'expérience
# valeur de référence

print("Valeur finale")
print("Masse de la Terre : ({:.1f} +/- {:.1f})e+24 kg".format(val_M_sim*1e-24, u_M*1e-24))
print("Z-score : {:.2f}".format(Z))

# Remarque 1
# Ici, une valeur de la mesure des dix périodes semble anormalement faible (6.66)
# Quand on moyenne les mesures avant de calculer M_Terre, son influence
# sur la valeur finale est plus faible que lorsqu'on fait la moyenne des valeurs
# de M_Terre avec ces mesures (parce que M_Terre varie comme 1/T**2).
# Ceci explique l'écart entre les deux valeurs val_M et val_M_sim.
# Sans raison valable pour exclure cette valeur, on doit cependant la garder.

# Remarque 2
# En faisant varier delta_l et delta_T, on s'apperçoit que c'est l'imprécision
# sur la mesure de T qui limite la précision du résultat obtenu.
# Je vous laisse imaginer comment on aurait pu améliorer le protocole expérimental...