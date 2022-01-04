import numpy as np
import numpy.random as rd

#######################
# RÉSULTATS DES MESURES
#######################
u       =  12.05    # tensions aux bornes de la résistance en volts
delta_u =   0.02    # imprécision sur la mesure de U en volts
i       = 125.1e-3  # intensité du courant en ampères
delta_i =   0.5e-3  # imprécision sur la mesure de I en ampères

#########################
# SIMULATION DE N MESURES
#########################
N = 10000
# N mesures de u équiréparties dans l'intervalle [u-du, u+du]
u_sim = rd.uniform(u-delta_u, u+delta_u, N)
# N mesures de i équiréparties dans l'intervalle [i-di, i+di]
i_sim = rd.uniform(i-delta_i, i+delta_i, N)

# fonction utilisée pour le calcul de la grandeur à partir des mesures
def resistance(u,i):
    return u/i      # loi d'ohm

r_sim = resistance(u_sim, i_sim) # calcul des N valeurs de R
val_r = np.mean(r_sim)           # moyenne des valeurs de R simulées
std_r = np.std(r_sim, ddof=1)    # écart-type expérimental

#######################
# AFFICHAGE DU RÉSULTAT
#######################
print("valeur de la résistance : R    = " + str(val_r) + " ohms")
print("incertitude-type        : u(R) = " + str(std_r) + " ohms")