import numpy as np
from numpy import exp
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.stats import sem

x= np.genfromtxt('Werte1.txt', unpack=True)

#Fehler auf alle Werte
x=unp.uarray(x, 0.1)
print(x)

#Differenzen
dx=np.diff(x)
print(dx)

#Wellenlänge= 2dx
l =2*dx
print(l)
ml=np.mean(l)
#ml=ml/1000
print('Mittelwert:', ml)
a=ufloat(22.860, 0.046)
print(a)
c=3*10**11
f=c*((1/(ml))**2 +(1/(2*a))**2)**0.5
print('f=', f)
#Wellenlänge frei
l0=c/f
print('l0=', l0 )
#Grenzwellenlänge lg=l
lc=l0/(1-(l0/ml)**2)
print('lc=', lc)

x1=ufloat(118.0, 0.1)
x2=ufloat(93.7, 0.1)
dx2=x1-x2
l2=2*dx2
print('l2=', l2)
#Stehwellenverhältnis
d1=ufloat(119.1, 0.1)
d2=ufloat(117.0, 0.1)
s=l2/(np.pi*(d1-d2))
print('S=', s)

a1=ufloat(20, 1)
a2=ufloat(43, 1)
s2=10*((a2-a1)/20)
print('s2=', s2)
#Dämpfung
#swr, d, eich= np.genfromtxt('Werte2.txt', unpack=True)
#dB=10*np.log10(swr)
