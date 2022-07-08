#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 16:44:59 2022
Causalité
@author: remimetzdorff
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def H(f,f0=1):
    """ Lowpass complex trasfer function """
    return 1 / (1 + 1j*f/f0)

def G(f,f0=1):
    """ Lowpass linear gain """
    return np.abs(H(f, f0=f0))

def square(t, f=1):
    """ Square signal """
    return np.sign(np.sin(2*np.pi*f*t))

def input_signal(t):
    e1 = square(t)
    e2 = np.sin(2*np.pi*t) + 0 * np.cos(2*np.pi*9*t)
    return e1

def ode(t,e,f0=1):
    def rc(V,t):
        return 2*np.pi*f0 * (e(t)-V[0])
    return odeint(rc, [e(0)], t)[:,0]

f0 = 5
N  = 2**18
t  = np.linspace(-50,50,N)
dt = t[1] - t[0]
freqs = np.fft.rfftfreq(N, dt)

e = input_signal(t)                      # Entrée
efft = np.fft.rfft(e)

sfft_causal = efft * H(freqs, f0=f0)     # Sortie calculée avec H
s_causal = np.fft.irfft(sfft_causal, n=N)

sfft_non_causal = efft * G(freqs, f0=f0) # Sortie calculée avec G
s_non_causal = np.fft.irfft(sfft_non_causal, n=N)

s_odeint = ode(t,input_signal,f0=f0)     # Sortie caclulée avec odeint
sfft_odeint = np.fft.rfft(s_odeint)

plt.figure(1, figsize=(8,4))
sps = (1,2)
ax1 = plt.subplot2grid(sps, (0,0))
ax2 = plt.subplot2grid(sps, (0,1))
ax1.set_xlim(0,2)
ax1.set_xlabel("Temps")
ax1.set_ylabel("Signal")
ax2.set_yticklabels([])
ax2.set_xlabel("Fréquence")
ax2.set_ylabel("Amplitude")
ax2.set_xlim(0,10)

if True:
    # entrée
    ax1.plot(t,e, "-C0", label="e")
    ax2.plot(freqs, np.abs(efft), "-oC0", label="e")

if True:
    # odeint
    ax1.plot(t,s_odeint, "-k", label="s (odeint)")
    ax2.plot(freqs, np.abs(sfft_odeint), "-ok", label="s (odeint)")

if True:
    # Complex transfer function
    ax1.plot(t,s_causal, "-C1", label="s (H)")
    ax2.plot(freqs, np.abs(sfft_causal), "-oC1", label="s (H)")

if True:
    # Linear gain only: no phase
    ax1.plot(t,s_non_causal, "-C2", label="s (G)")
    ax2.plot(freqs, np.abs(sfft_non_causal), "-oC2", label="s (G)")

for ax in [ax1, ax2]:
    ax.legend(loc="upper right")
    
plt.show()
