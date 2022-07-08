#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 17:51:24 2022
TD17 exo10 (correction)
@author: remimetzdorff
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

theta0 = 5 * np.pi/180
def f(theta):
    return 1 / np.sqrt(np.cos(theta0) - np.cos(theta))

def rectangle_gauche(f, a, b, n):
    x = np.linspace(a, b-(b-a)/n, n)
    return (b-a) / n * np.sum(f(x))
def rectangle_milieu(f, a, b, n):
    x = np.linspace(a, b-(b-a)/n, n) + (b-a)/n/2
    return (b-a) / n * np.sum(f(x))

# La méthode des rectangles à gauche ne fonctionne pas ici
# car la fonction f tend vers l'infini en theta0
print(rectangle_milieu(f, theta0, np.pi/2, 1000000))
# Le résultat est proche de celui donné avec la fonction quad
I_quad = quad(f, theta0, np.pi/2)[0]
print(I_quad)

n = [ 2**k for k in range(20) ]
I = [ rectangle_milieu(f, theta0, np.pi/2, k) for k in n ]
plt.semilogx(n, I, "o", label="rectangle au milieu")
plt.semilogx(n, np.ones(len(n)) * I_quad, "--", label="quad")
plt.xlabel("$n$")
plt.ylabel("Valeur de l'intégrale")
plt.legend()
plt.grid()
plt.show()