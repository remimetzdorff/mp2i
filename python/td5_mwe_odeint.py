"""td5_mwe_odeint.py"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#############################
# PARAMÈTRES DE LA RÉSOLUTION
#############################
t0 = 0                   # bornes de l'intervalle de résolution
tf = 5                   # en secondes
dt = 1e-3                # pas de temps en secondes
n  = int((tf-t0)/dt + 1) # nombre de points
t = np.linspace(t0,tf,n) # temps en secondes
X0 = [1,0]               # conditions initiales : [u(0), du(0)/dt]
omega0 = 2 * np.pi * 1   # pulsation propre en s^-1

###############################################
# FONCTION ASSOCIÉE À L'ÉQUATION DIFFÉRENTIELLE
###############################################
def F(V, t):
    x, y = V        # vecteur V : v[0] = u, v[1] = du/dt
    dx = y          # dx/dt
    dy = -omega0 ** 2 * x # dy/dt
    dV = [dx, dy]   # vecteur dV/dt : dV[0] = du/dt, dV[1] = d2u/dt2 
    return dV

########################################
# RÉSOLUTION ET REPRÉSENTATION GRAPHIQUE
########################################
X = odeint(F, X0, t) # résolution
u = X[:,0]           # récupération des données
plt.plot(t, u)
plt.xlabel("Temps (s)")
plt.ylabel("Tension (V)")