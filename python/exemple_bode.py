import numpy as np
import matplotlib.pyplot as plt

def lowpass(f,f0):
    return 1 / (1 + 1j * f / f0)

f = np.logspace(1,6)
h = lowpass(f,10e3)
g = 20 * np.log10(np.abs(h))
phi = np.angle(h) * 180 / np.pi

plt.figure()
sps = (3,1)
ax1 = plt.subplot2grid(sps, (0,0),rowspan=2)
ax2 = plt.subplot2grid(sps, (2,0))

ax1.semilogx(f, g)
ax1.set_xlim(1e3,1e5)
ax1.set_ylim(-20,2)
ax1.set_xticklabels([])
ax1.set_title("Passe-bas d'ordre 1")
ax1.grid(which="both")
ax1.set_ylabel("Gain (dB)")

ax2.semilogx(f,phi)
ax2.grid(which="both")
ax2.set_xlim(1e3,1e5)
ax2.set_xlabel("Fréquence (Hz)")
ax2.set_ylabel("Phase (°)")

plt.figure()
plt.plot(g, phi)

plt.show()