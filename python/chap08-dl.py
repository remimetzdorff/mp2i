#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 19:54:11 2021
Développement limité
@author: remimetzdorff
"""

import numpy as np
import matplotlib.pyplot as plt

N = 20 # ordre du DL

def factorial(n):
    fact = 1
    for k in range(1,n+1):
        fact *= k
    return fact

def cosDL(x,N):
    y = np.zeros(len(x))
    for n in range(N+1):
        if n%2 == 0:
            y += (-1)**(n/2) * x**n / factorial(n)
    return y

x = np.linspace(-2*np.pi,2*np.pi,1000)

plt.plot(x, np.cos(x),"k")
plt.plot(x, cosDL(x,N), label="ordre "+str(N))

plt.ylim(-1.1,1.1)
plt.xlabel("$x$")
plt.ylabel("$\cos(x)$")
plt.legend()
plt.title("Développement limité de $\cos(x)$ au voisinage de 0")
plt.show()