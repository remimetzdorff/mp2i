# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

#########################
# IMPORTATION DES DONNÉES
#########################
filename = "scope_0.csv" # nom du fichier contenant les données
data = np.genfromtxt(filename, delimiter=',')
t    = data[2:,0]        # temps en secondes
ch1  = data[2:,1]        # tension mesurée sur le canal 1, en volts
ch2  = data[2:,2]        # tension mesurée sur la canal 2, en volts
N    = len(t)            # nombre de points
dt   = t[1] - t[0]       # intervalle de temps entre deux points (s)

############################################
# CHOIX DES DONNÉES UTILES POUR L'AJUSTEMENT
############################################
start  = -0.049    # début de la portion utile, en secondes
stop   = -0.035     # fin de la portion utile, en secondes
nstart = int((start - t[0]) / dt)
nstop  = int((stop - t[0]) / dt)
x      = t[nstart:nstop]    # selection d'une partie seulement des données
y      = ch2[nstart:nstop]

##########################
# REPRÉSENTATION GRAPHIQUE
##########################
plt.figure()
plt.plot(t, ch1, label="CH1")
plt.plot(t, ch2, label="CH2")
plt.plot(x, y, label="Données utilisées pour l'ajustement")

plt.xlabel("Temps (s)")
plt.ylabel("Tension (V)")
plt.title("Données brutes")
plt.legend(loc="upper right")

#####################
# AJUSTEMENT LINÉAIRE
#####################
plt.figure()
a, b = np.polyfit(x,np.log(y),1) # Ajustement des données sous la forme y = a * x + b
plt.plot(x, np.log(y), label="Données")
plt.plot(x, a*x+b, label="Ajustement")

plt.xlabel("Temps (s)")
plt.title("Ajustement linéaire")
plt.legend(loc="upper right")

print(-1/a)

plt.show()