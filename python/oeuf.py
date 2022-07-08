import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.animation as anim

w = 5 #la vitesse angulaire
mu=0.3
q=0.5 #le paramètre à optimiser
k=mu*q
t0=10 #encore un paramètre, on peut aussi jouer dessus
T=5*t0 #durée totale de la simulation, à augmenter si elle se termine avant que l'oeuf soit stabilisé en position haute
N=300 #nombre de points (à modifier si nécéssaire)
(p,q)=(20,20) #resolution de la grille, il faut juste savoir que très rapidement ça tourne plus avec une machine normale
n=0
tau=T/N


def Thet(k,t,t0):
    return np.arctan(np.exp(-k*(t-t0)))

r = 0.3

phi, theta = np.mgrid[0.0:np.pi:1j*p, -np.pi:np.pi:1j*q]
x = 2*r*np.cos(theta)
y = r*0.4*(2.5+1/3*theta**2)*np.sin(theta)*np.sin(phi)
z = r*0.4*(2.5+1/3*theta**2)*np.sin(theta)*np.cos(phi)


fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
line=ax.plot_surface(x,y,z,rstride=1,cstride=1,color='lightblue',alpha=0.5,linewidth=0)
plt.tight_layout()
ax.set_xlim3d([-1,1])
ax.set_ylim3d([-1,1])
ax.set_zlim3d([-1,1])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

def update(n): #la fonction qui actualise l'état de l'oeuf à chaque itération
    n+=1
    t=n*tau
    thet=Thet(k,t,t0)
    x2 = np.cos(np.pi/2-thet)*x - np.sin(np.pi/2-thet)*z
    y2 = y
    z2 = np.sin(np.pi/2-thet)*x + np.cos(np.pi/2-thet)*z
    m=np.min(z2)
    x3 = np.cos(w*t)*x2 - np.sin(w*t)*y2
    y3 = np.sin(w*t)*x2 + np.cos(w*t)*y2
    z3 = z2-m
    ax.clear()
    ax.set_xlim3d([-1,1])
    ax.set_ylim3d([-1,1])
    ax.set_zlim3d([-1,1])
    line=ax.plot_surface(x3,y3,z3,rstride=1,cstride=1,color='lightblue',alpha=0.5,linewidth=0) #la variable qui stocke l'état de la figure
    return line,

animation=anim.FuncAnimation(fig,update,frames=N,interval=tau,repeat=False) #frames = nombre d'itération,interval = FPS en ms

plt.show()



