#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 23:19:47 2022
DM11 - Exercice 2 (TP24)
@author: remimetzdorff
"""

import numpy as np
import matplotlib.pyplot as plt

# Lecture d'un fichier de données
data = np.genfromtxt("etalonnage.csv", delimiter=";", skip_header=2)
x, y = data[:,0], data[:,1]

plt.plot(x, y, "o")
plt.show()