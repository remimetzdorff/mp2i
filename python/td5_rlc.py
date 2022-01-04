import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#############################
# PARAMÈTRES DE LA RÉSOLUTION
#############################
t0 = 0
tf = 3
dt = 1e-3
t  = np.arange(t0,tf,dt)

##########################
# PARAMÈTRES DU CIRCUIT LC
##########################
omega0 = 2*np.pi*10 # pulsation propre en s^-1
Q      = 15
u0  = 1            # CI : tension aux bornes du condensateur en V
du0 = 0            #      dérivée première de la tension en V/s
V0  = [u0,du0]

E = 0.5
omega = .02 * omega0

###############################################
# FONCTION ASSOCIÉE À L'ÉQUATION DIFFÉRENTIELLE
###############################################
def oa_sans_source(V,t):
    x,y = V
    dx = y
    dy = -omega0**2 * x - omega0/Q * y 
    dV = [dx, dy]
    return dV

V = odeint(oa_sans_source, V0, t)
u = V[:,0]

#plt.plot(t, np.sign(np.sin(omega*t)))
plt.plot(t,u)
plt.xlabel("Temps (s)")
plt.ylabel("Tension u(t) (V)")