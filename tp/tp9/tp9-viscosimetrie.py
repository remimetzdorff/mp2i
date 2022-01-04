import numpy as np

# Constantes
g = 9.81       # accélération de pesanteur en m.s^-2
rho_a = 7.83e3 # masse volumique de l'acier en kg.m^-3
rho_g = 1.3e3  # masse volumique du glycérol en kg.m^-3

#####################################################
# Paramètres à adapter aux conditions de l'expérience
#####################################################
r = 1e-3       # rayon de la bille en mètre
delta_r = 0    # imprécision sur la mesure de r en mètre
L = 1e-2       # distance entre les deux repères du viscosimètre en mètre
delta_L = 0    # imprécision sur la mesure de L en mètre

##########################
# Mesures de dt en seconde
##########################
dt = [1]
tab_dt = np.array(dt)
delta_dt = 0   # imprécision sur la mesure de dt en seconde

def viscosite_dynamique(dt,r,L):
    """calcule la viscosité dynamique en Pa.s
    lors d'une expérience avec un viscosimètre à chute de bille"""
    return 2/9 * r**2*g/L * (rho_a - rho_g) * dt

#######################
# Incertitude de type A
#######################
# À compléter
print("Estimation de type de A :")

# Estimation de l'incertitude de type B
N = 10000
r_sim = r + np.random.uniform(-delta_r,delta_r,N)
L_sim = L + np.random.uniform(-delta_L,delta_L,N)
dt_sim = np.mean(dt) + np.random.uniform(-delta_dt,delta_dt,N)
eta_sim = viscosite_dynamique(dt_sim,r_sim,L_sim)

print("Estimation de type de B :")
print("eta    = {:.2f} Pa.s".format(np.mean(eta_sim)))
print("u(eta) = {:.2f} Pa.s".format(np.std(eta_sim,ddof=1)))