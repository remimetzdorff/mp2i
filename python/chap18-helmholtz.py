#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 09:41:35 2022
Configuration Helmholtz
@author: remimetzdorff
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

def Bspire(z):
    return  1 / ((1 + z**2) ** (3/2))

def Bhelmholtz(z, d):
    Bg = Bspire(z-d/2)
    Bd = Bspire(z+d/2)
    return Bg + Bd

# Define initial parameters
z = np.linspace(-2,2, 1000)
init_d = 0.25

# Create the figure and the line that we will manipulate
fig, ax = plt.subplots()
line_Bg, = plt.plot(z, Bspire(z-init_d/2))
line_Bd, = plt.plot(z, Bspire(z+init_d/2))
line_Bh, = plt.plot(z, Bhelmholtz(z, init_d))
ax.set_xlabel("$z^*$")
ax.set_ylabel("$B_z^*$")
ax.set_xlim(min(z),max(z))
#ax.set_ylim(-2.5,2.5)
ax.set_title("Champ magnétique sur l'axe de deux spires")
ax.grid()

# adjust the main plot to make room for the sliders
plt.subplots_adjust(bottom=0.25)

# Make a horizontal slider to control the omega.
axd = plt.axes([0.125, 0.1, 0.775, 0.03])
dslider = Slider(
    ax=axd,
    label="$d^*$",
    valmin=0,
    valmax=5,
    valinit=init_d,
)

# The function to be called anytime a slider's value changes
def update(val):
    line_Bg.set_ydata(Bspire(z - dslider.val/2))
    line_Bd.set_ydata(Bspire(z + dslider.val/2))
    line_Bh.set_ydata(Bhelmholtz(z, dslider.val))
    fig.canvas.draw_idle()

# register the update function with each slider
dslider.on_changed(update)

# Create a `matplotlib.widgets.Button` to reset the sliders to initial values.
resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button_reset = Button(resetax, 'Reset', hovercolor='0.975')

def reset(event):
    dslider.reset()
button_reset.on_clicked(reset)

plt.show()