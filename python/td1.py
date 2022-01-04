import numpy as np
import matplotlib.pyplot as plt

i = 30       # angle d'incidence en degrés
n_air = 1.00 # indice optique de l'air
n_eau = 1.33 # indice optique de l'eau

##########################
# Préparation de la figure
##########################
fig = plt.figure(figsize=(6,4))
plt.xlim(-1.5,1.5)
plt.ylim(-1,1)
plt.gca().set_aspect('equal') # même échelle sur les deux axes
# Le décor
plt.plot([-2,2], [0,0], "-k")
plt.fill_between([-2,2], 0,-2, color="C0", alpha=0.25)
plt.plot([0,0], [-2,2], "--k", alpha=0.2) # normale au dioptre

#################
# Tracé de rayons
#################
# rayon incident
xa = #À COMPLÉTER#      # abscisse du point A
ya = #À COMPLÉTER#      # ordonnée du point A
plt.plot([xa,0], [ya,0])

plt.show() # pour afficher le graphique