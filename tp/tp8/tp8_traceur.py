# tp8_traceur.py
# Ce programme permet :
#   - lire un fichier de donnée .txt ;
#   - représenter graphiquement les données ;
#   - dériver une gradeur par rapport au temps ;

import numpy as np
import matplotlib.pyplot as plt

def deriv(x,t):
    """calcule la dérivée numérique des valeurs de x par rapport à t"""
    dt = np.diff(t)      # valeurs de dt
    dx = np.diff(x)      # valeurs de x(t+dt) - x(t)
    return dx/dt, t[:-1] # dérivée (x(t+dt) - x(t)) / dt

def norme(x,y):
    """calcule la norme d'un vecteur (x,y)"""
    return # À compléter

#########################
# IMPORTATION DES DONNÉES
#########################
filename = "rampe_prof.txt"
data     = np.loadtxt(filename, skiprows=1)
temps_pos = data[:,0]
pos_x     = data[:,1]
pos_y     = data[:,3]

##########################
# REPRÉSENTATION GRAPHIQUE
##########################
plt.plot(temps_pos, pos_x, "o")
plt.xlabel("Temps (s)")
plt.ylabel("Position $y$ (m)")
plt.title("Mouvement d'une balle sur une rampe")