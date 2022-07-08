#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 00:00:51 2022
Lecture d'un fichier de donnée
@author: remimetzdorff
"""

import numpy as np
import matplotlib.pyplot as plt

# Lecture du fichier de donnée
data = np.loadtxt("data.txt",skiprows=1)
f = data[:,0] # première colonne : fréquence en Hz
e = data[:,1] # deuxième colonne : tension aux bornes du GBF en V
u = data[:,2] # troisième colonne : tension aux bornes de R ou C en V
G = u/e

# Représentation graphique avec une échelle logarithmique pour la fréquence
# Il suffit de remplacer plt.plot par plt.semilogx
# Pour que l'axe des ordonnées soit en échelle log, utiliser plt.semilogy
# Pour un tracer loglog, utiliser plt.loglog
plt.semilogx(f,G,"o")

# À compléter (titre, nom des axes, etc.)