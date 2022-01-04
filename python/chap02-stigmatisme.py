import numpy as np
import matplotlib.pyplot as plt

# PARAMÈTRES
radius = 1   # rayon du dioptre sphérique
n = 1.5      # indice de la lentille
N = 200      # nb de rayons lumineux
alpha = 0.05 # transparence rayons
frac = 0.8   # fraction du rayon de la lentille utilisé

# figure layout
plt.figure(figsize=(12,8))
ax = plt.subplot2grid((1,1), (0,0))
ax.set_aspect("equal")
ax.set_xlim(-1*radius, 5*radius)

# dioptre sphérique
y = np.linspace(-1,1,101) * 0.9 * radius
x = np.sqrt(radius ** 2 - y ** 2)
ax.plot([-radius, 2*radius], np.zeros(2), "k")
ax.plot(x,y,"C0")
ax.plot([np.min(x), np.min(x)], [np.min(y), np.max(y)], "C0")

# rayons
height  = np.linspace(-frac * radius, frac * radius, N)
for h in height:
    xd = np.sqrt(radius ** 2 - h ** 2)
    i = np.arcsin(h / radius)
    r = np.arcsin(h / radius / n)
    xf = xd - h / np.tan(r-i)
    ax.plot([-radius, xd, xf, 2 * xf - xd], [h, h, 0, -h], "red", alpha=alpha)

plt.show()