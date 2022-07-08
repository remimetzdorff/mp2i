#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 18:16:18 2022
TP28 Enthalpie massique de fusion de l'eau
Estimation de type A
@author: remimetzdorff
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("enthalpie_fusion.txt", skiprows=2)

vals, uvals = data[:,0], data[:,1]


plt.hist(vals)
