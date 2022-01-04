import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#######################
# PARAMÈTRES DU CIRCUIT
#######################
E = 12 # en V donnée de l'énoncé
r = 6  # en ohms, donnée de l'énoncé
omega0 = 2*np.pi / 4e-3  # en s^-1, lecture graphique
Q      = 13              # facteur de qualité, essais-erreur
L   = r * Q / omega0     # en H
C   = 1 / r / Q / omega0 # en F
I1 = E/r                 # en A
mu     = omega0 / 2 / Q  # valeur absolue de la partie réelle de la racine
omega  = omega0 * np.sqrt(1 - 1/4/Q**2) # partie imaginaire

############
# RÉSOLUTION
############
def charge_primaire(V, t):
    """Fonction associée à l'équation différentielle"""
    x, y = V
    dx = y
    dy = - omega0 / Q * y - omega0**2 * x + omega0**2 * C*E
    dV = [dx, dy]
    return dV

t = np.linspace(0, 30e-3, 1000)
V0 = [0,I1]
V = odeint(charge_primaire, V0, t)
q_num = V[:,0]

def q_ana(t):
    """Expression analytique de la charge du condensateur"""
    fact_exp = np.exp(-mu*t)
    A = - C*E
    B = (I1 - mu * C * E) / omega
    return fact_exp * (A * np.cos(omega*t) + B * np.sin(omega*t)) + C*E

##########################
# REPRÉSENTATION GRAPHIQUE
##########################
plt.plot(t*1e3,q_num*1e3, label="Numérique")
plt.plot(t*1e3,q_ana(t)*1e3, label="Analytique")
plt.xlabel("Temps $t$ (ms)")
plt.ylabel("Charge du condenstaeur $q$ (mC)")
plt.title("Évolution de la charge du condensateur")
plt.legend()