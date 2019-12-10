import numpy as np
from numpy import exp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.stats import sem
from math import e
import scipy.integrate as integrate

l1, x1, y1, t1= np.genfromtxt('Werte2.txt', unpack=True)
l2, x2, y2 ,t2= np.genfromtxt('Werte3.txt', unpack=True)
l3, x3, y3, t3= np.genfromtxt('Werte4.txt', unpack=True)

d1=(y1-x1)/2
d2=(y2-x2)/2
d3=(y3-x3)/2

print(d1)

a2=ufloat(0.0137903974304,0.0014476904771)
a1=ufloat(0.00717245083481,0.000875814923637)
e=1.602176634*10**(-19)
eps=8.8541878128*10**(-12)
n1=1.2*10**(24)
n2=2.8*10**(24)
c=299792458
m=9.1093837015*10**(-31)
i1=3.4744
i2=3.4078
i3=3.3820
i4=3.3551
i5=3.3404
i6=3.3321
i7=3.3261
i8=3.3187
i=(3.4744,3.4078,3.3820,3.3551,3.3404,3.3321,3.3261,3.3187)
ges=0
for m in range (0,8):
    w1=(e**3*n1*0.436/(8*np.pi**2*eps*c**3*i[m]*1000*a1*10**12))**(1/2)
    w2=(e**3*n2*0.436/(8*np.pi**2*eps*c**3*i[m]*a2*1000*10**12))**(1/2)
    print(w1,w2)
    ges=ges+w1+w2

Nam=(6.8,6.8,6.9,6.9,6.9,6.9,6.9,6.9,7.5,7.5,7.6,7.6,7.6,7.6,7.6,7.6)


mw=np.mean(Nam)
mwf=sem(Nam)
gesf=(0.4)**(1/2)
#print(7*10**(-32)/(9.1093837015*10**(-31)))
ges=ges/16
eff=ufloat(7.2*10**(-32),0.4*10**(-32))
ver=eff/(9.1093837015*10**(-31))
print(mw, mwf, ges, gesf,ver)
