import numpy as np
import matplotlib.pyplot as plt

#############################
# PARAMÈTRES DE LA RÉSOLUTION
#############################
t0 = 0                   # bornes de l'intervalle de résolution
tf = 1                   # en secondes
dt = 1e-4                # pas de temps en secondes
n  = int((tf-t0)/dt + 1) # nombre de points
t = np.linspace(t0,tf,n) # temps en secondes

##########################
# PARAMÈTRES DU CIRCUIT RC
##########################
u0  = 1   # u(0) en volts (CI)
tau = 0.1 # temps caractéristique en secondes

############
# SIGNAL GBF
############
E   = 0   # offset en volts
amp = 1   # amplitude en volts
f   = 1   # fréquence en hertz

constant = np.ones(n) * E
square   = amp * np.sign(np.sin(2*np.pi*f*t)) + E
sinus    = amp * np.sin(2*np.pi*f*t) + E
noise    = np.random.normal(0,0.005,n) # bruit aléatoire
e = constant + noise # signal aux bornes du GBF
# À vous de créer le signal que vous voulez tester...

#################
# MÉTHODE D'EULER
#################
u = np.zeros(len(t))  # préparation du tableau
u[0] = u0             # initialisation en fonction de la CI
for i in range(n-1):  # méthode d'Euler explicite
    u[i+1] = e[i] * dt / tau + u[i] * (1 - dt / tau)

##########################
# REPRÉSENTATION GRAPHIQUE
##########################
plt.plot(t,e, label="e(t)")
plt.plot(t,u, label="u(t)")
plt.xlabel("Temps (s)")
plt.ylabel("Tension (V)")
plt.legend()
plt.show() # pour afficher le graphique