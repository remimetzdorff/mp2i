#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 19:03:33 2022
Résonance en tension aux bornes du condensateur avec Slider
@author: remimetzdorff
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

omega0 = 2*np.pi
t = np.linspace(0,10*2*np.pi/omega0,10000)

def e(t,f):
    return np.cos(2*np.pi*f * t)

def h(f,Q):
    x = 2*np.pi*f/omega0
    return 1 / (1 - x**2 + 1j*x/Q)

def s(t,f,Q):
    H = h(f,Q)
    g = np.abs(H)
    phi = np.angle(H)
    return g * np.cos(2*np.pi*f * t + phi)

# Define initial parameters
init_freq = 1
init_Q    = 1 / np.sqrt(2)

# Create the figure and the line that we will manipulate
fig, ax = plt.subplots()
line_e, = plt.plot(t, e(t, init_freq))
line_s, = plt.plot(t, s(t, init_freq, init_Q))
ax.set_xlabel("Temps (s)")
ax.set_ylabel("Amplitude")
ax.set_xlim(0,10*2*np.pi/omega0)
ax.set_ylim(-2.5,2.5)
ax.set_title("Résonance en tension aux bornes du condensateur")

# adjust the main plot to make room for the sliders
plt.subplots_adjust(left=0.25, bottom=0.25)

# Make a horizontal slider to control the omega.
axfreq = plt.axes([0.25, 0.1, 0.65, 0.03])
freq_slider = Slider(
    ax=axfreq,
    label="$f (Hz)$",
    valmin=1e-4,
    valmax=2,
    valinit=init_freq,
)

# Make a vertically oriented slider to control the Q
axQ = plt.axes([0.1, 0.25, 0.0225, 0.63])
Q_slider = Slider(
    ax=axQ,
    label="$Q$",
    valmin=1e-4,
    valmax=10,
    valinit=init_Q,
    orientation="vertical"
)
ax.set_ylim(-1.1*Q_slider.valmax,1.1*Q_slider.valmax)

# The function to be called anytime a slider's value changes
def update(val):
    line_e.set_ydata(e(t, freq_slider.val))
    line_s.set_ydata(s(t, freq_slider.val, Q_slider.val))
    fig.canvas.draw_idle()

# register the update function with each slider
freq_slider.on_changed(update)
Q_slider.on_changed(update)

# Create a `matplotlib.widgets.Button` to reset the sliders to initial values.
resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button_reset = Button(resetax, 'Reset', hovercolor='0.975')

def reset(event):
    freq_slider.reset()
    Q_slider.reset()
button_reset.on_clicked(reset)

plt.show()