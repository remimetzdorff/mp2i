import numpy as np
import matplotlib.pyplot as plt

#######################
# GÉNÉRATION DE DONNÉES
#######################
x0    = 1.0
sigma = 0.1
n     = 100

r = np.random.normal(x0, sigma, n)

#########################
# HISTOGRAMME DES DONNÉES
#########################
# A compléter

plt.xlabel("Le titre de l'axe des abscices")
plt.ylabel("Le titre de l'axe des ordonnées")
plt.title("Le titre du graphique")
plt.show()