#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 15:38:40 2022
https://www.f-legrand.fr/scidoc/docmml/sciphys/elecmag/pyspire/pyspire.html
@author: remimetzdorff
"""

import math 
import numpy
from scipy.integrate import odeint
from scipy.special import ellipk, ellipe
from matplotlib.pyplot import *

class Spire:
    def __init__(self,a,zs,i):
        self.a = a
        self.a2 = a*a
        self.a4 = self.a2*self.a2
        self.zs = zs
        self.i = i
    def champB(self,x,z):
        if abs(x) < 1e-8:
            x=0
        if x>0:
            sx = 1
            x = -x
        else:
            sx = -1
        z = z-self.zs
        x2 = x*x
        z2 = z*z
        r2 = x2+z2
        b1 = self.a2+ r2
        b2 = 2*x*self.a
        b3 = b1+b2
        b4 = b1-b2
        b5 = -2*b2/b4
        b6 = math.sqrt(b3/b4)*self.i 
        rb3 = math.sqrt(b3)
        b7 = self.a*b3*rb3
        b8 = self.a4-self.a2*(x2-2*z2)+z2*(x2+z2)
        b9 = (self.a2+z2)*b3
        e = ellipe(b5)
        k = ellipk(b5)
        bz = b6*((self.a2-r2)*e+b3*k)/b7
        if x==0:
            bx = 0.0
            Atheta = 0.0
            Adx = bz/2
        else:
            bx = -sx*z/x*b6*(b1*e-b3*k)/b7
            Atheta = -sx*b6/x*(-b4*e+(self.a2+r2)*k)/(self.a*rb3)
            Adx = b6/x2*(b8*e-b9*k)/b7
        return [bx,bz,Atheta,Adx]
    
class SystemeSpires:
    def __init__(self,xmin,xmax,zmin,zmax):
        self.xmin = xmin
        self.xmax = xmax
        self.zmin = zmin
        self.zmax = zmax
        self.spires = []
        self.n = 0
    def bornes(self,xmin,xmax,zmin,zmax):
        self.xmin = xmin
        self.xmax = xmax
        self.zmin = zmin
        self.zmax = zmax
    def ajouter(self,spire):
        self.spires.append(spire)
        self.n += 1
    def champB(self,x,z):
        bx = 0.0
        bz = 0.0
        A = 0.0
        Adx = 0.0
        for spire in self.spires:
            b = spire.champB(x,z)
            bx += b[0]
            bz += b[1]
            A += b[2]
            Adx += b[3]
        return [bx,bz,A,Adx]
    def normeB(self,x,y):
        Bx, Bz, _, _ = self.champB(x, z)
        return np.sqrt(Bx**2 + Bz**2)
    
    def Bz_z(self,x,z):
        nz = len(z)
        bz = numpy.zeros(nz)
        for k in range(nz):
            b = self.champB(x,z[k])
            bz[k] = b[1]
        return bz
    
    def Bz_x(self,x,z):
        nx = len(x)
        bz = numpy.zeros(nx)
        for k in range(nx):
            b = self.champB(x[k],z)
            bz[k] = b[1]
        return bz
    def Bx_z(self,x,z):
        nz = len(z)
        bx = numpy.zeros(nz)
        for k in range(nz):
            b = self.champB(x,z[k])
            bx[k] = b[0]
        return bx
    def Bx_x(self,x,z):
        nx = len(x)
        bx = numpy.zeros(nx)
        for k in range(nx):
            b = self.champB(x[k],z)
            bx[k] = b[0]
        return bx
    def A_x(self,x,z):
        nx = len(x)
        A = numpy.zeros(nx)
        for k in range(nx):
            b = self.champB(x[k],z)
            A[k] = b[2]
        return A
    def Adx_x(self,x,z):
        nx = len(x)
        Adx = numpy.zeros(nx)
        for k in range(nx):
            b = self.champB(x[k],z)
            Adx[k] = b[3]
        return Adx
    
    def B(self,x,z):
        nx = len(x)
        nz = len(z)
        bx = numpy.zeros((nx,nz))
        bz = numpy.zeros((nx,nz))
        A = numpy.zeros((nx,nz))
        for i in range(nz):
            for j in range(nx):
                b = self.champB(x[j],z[i])
                bx[j][i] = b[0]
                bz[j][i] = b[1]
                A[j][i] = b[2]
        return [bx,bz,A]
    
    def ligneB(self,x0,z0,sens):
        def equation(y,t):
            b = self.champB(y[0],y[1])
            nb = math.sqrt(b[0]*b[0]+b[1]*b[1])
            return [sens*b[0]/nb,sens*b[1]/nb]
        tmax = (self.xmax-self.xmin)
        te = 1.0*tmax/100
        xarray = numpy.array([x0])
        zarray = numpy.array([z0])
        x=x0
        z=z0
        t = 0.0
        while t < tmax:
            y = odeint(equation,[x,z],[0,te],rtol=1e-5,atol=1e-5)
            x = y[1][0]
            z = y[1][1]
            if x<self.xmin or x>self.xmax or z<self.zmin or z>self.zmax:
                break
            xarray = numpy.append(xarray,x)
            zarray = numpy.append(zarray,z)
            t += te
        return [xarray,zarray]
    
    def plot_lignes(self,points,style):
        for p in points:
            [x,z] = self.ligneB(p[0],p[1],1)
            plt.plot(z,x,style)
            [x,z] = self.ligneB(p[0],p[1],-1)
            plt.plot(z,x,style)
            plt.arrow(z[0], x[0], z[1], x[1]-x[0], shape='full', lw=0, length_includes_head=True, head_width=.15, color="C0")
            [x,z] = self.ligneB(-p[0],p[1],1)
            plt.plot(z,x,style)
            [x,z] = self.ligneB(-p[0],p[1],-1)
            plt.plot(z,x,style)
            plt.arrow(z[0], x[0], z[1], x[1]-x[0], shape='full', lw=0, length_includes_head=True, head_width=.15, color="C0")
            for s in self.spires:
                plot([s.zs,s.zs],[-s.a,s.a],linestyle=" ",marker=".",color="black")

L = 1
N = 2

systeme = SystemeSpires(-5.0,5.0,-5.0,5.0)
for z in np.linspace(-L/2,L/2,N):
    systeme.ajouter(Spire(1,z,1.0))

figure(figsize=(7,7))
vals = np.linspace(0,.8,7)
points = [[val, 0, 0] for val in vals]
systeme.plot_lignes(points,'C0')
plt.xlim(-5,5)
plt.ylim(-5,5)
plt.xlabel('z')
plt.ylabel('r')
            