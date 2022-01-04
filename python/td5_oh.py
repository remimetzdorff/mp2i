import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint # pour la résolution d'éq diff

#############################
# PARAMÈTRES DE LA RÉSOLUTION
#############################
t0 = 0                   # bornes de l'intervalle de résolution
tf = 1
dt = 1e-3                # pas de temps en secondes
n  = int((tf-t0)/dt + 1) # nombre de points
t = np.linspace(t0,tf,n) # temps en seconde

##########################
# PARAMÈTRES DU CIRCUIT LC
##########################
omega0 = 2*np.pi*5 # pulsation propre en s^-1
u0  = 1            # CI : tension aux bornes du condensateur en V
du0 = 0            #      dérivée première de la tension en V/s
V0  = [u0,du0]

###############################################
# FONCTION ASSOCIÉE À L'ÉQUATION DIFFÉRENTIELLE
###############################################
def oh(V, t):       # oscillateur harmonique
    x, y = V        # vecteur V : v[0] = u, v[1] = du/dt
    dx = y
    dy = - omega0**2 * x
    dV = [dx, dy]   # vecteur dV/dt : dV[0] = du/dt, dV[1] = d2u/dt2
    return dV

############
# RÉSOLUTION
############
# Euler explicite (cf TD4)
def euler_explicite(t):
    x = np.zeros(len(t)) # x = u
    y = np.zeros(len(t)) # y = du/dt
    x[0] = V0[0]         # initialisation avec les CI
    y[0] = V0[1]
    for k in range(len(t)-1):
        dx, dy = oh([x[k], y[k]], t) # calcul des valeurs de du/dt
                                     # et d2u/dt2 à l'instant k
        x[k+1] = x[k] + dt * dx      # calcul de du/dt en k+1
        y[k+1] = y[k] + dt * dy      # calcul de d2u/dt2 en k+1
    return x, y
# Euler implicite (Hors programme)
def euler_implicite(t):
    x = np.zeros(len(t))
    y = np.zeros(len(t))
    x[0] = V0[0]
    y[0] = V0[1]
    for k in range(len(t)-1):
        x[k+1] = (x[k] + dt * y[k]) / (1 + omega0**2 * dt**2)
        y[k+1] = (y[k] - omega0**2*dt*x[k]) / (1 + omega0**2 * dt**2)
    return x, y

##########################
# REPRÉSENTATION GRAPHIQUE
##########################
# Analytique
plt.plot(t, np.cos(omega0*t), label="analytique")
# Euler explicite
u, du = euler_explicite(t)
plt.plot(t, u, label="euler expl")
# Euler implicite
u, du = euler_implicite(t)
plt.plot(t, u, label="euler impl")
# odeint
V = odeint(oh, V0, t) # résolution avec odeint de scipy.integrate
u = V[:,0]            # récupération des valeurs de u(t)
plt.plot(t, u, label="odeint")

plt.title("Évolution de la tension dans un circuit LC sans source")
plt.xlabel("Temps (s)")
plt.ylabel("Tension (V)")
plt.legend(loc="lower left")