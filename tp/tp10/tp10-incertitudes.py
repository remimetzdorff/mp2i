import numpy as np

########################
# MESURES ET IMPRÉCISION
########################
T = 0.5          # période des oscillations (s)
delta_T = 0.1    # imprecision sur la mesure de T (s)
m = 200e-3       # masse (kg)
delta_m = 0.1e-3 # imprécision sur la mesure de m (kg)

def raideur(T, m):
    """calcule la constante de raideur k d'un ressort, en N/m
        T : période des oscillations (s)
        m : masse (kg)
    """
    return 4 * np.pi**2 * m / T**2

#######################################
# ESTIMATION DE L'INCERTITUDE DE TYPE B
#######################################
N = 10000
T_sim = T + np.random.uniform(-delta_T,delta_T,N)
m_sim = m + np.random.uniform(-delta_m,delta_m,N)
k_sim = raideur(T_sim,m_sim)

print("Estimation de type de B :")
print("k    = {:.2f} N/m".format(np.mean(k_sim)))
print("u(k) = {:.2f} N/m".format(np.std(k_sim,ddof=1)))