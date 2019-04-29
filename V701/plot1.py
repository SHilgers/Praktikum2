import numpy as np
from numpy import exp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.stats import sem

p, Emax, N= np.genfromtxt('Werte1.txt', unpack=True)
x1, N1= np.genfromtxt('Werte11.txt', unpack=True)

#Berechnung der Energien,nach linearer Skala in MeV
E0=4
E1=E0/540
E=E1*Emax
print('Energien der alpha-Teilchen=', E)

#Berechnung Mittlere Reichweite R
#R=3.1*((Emax)**(3/2))
#print('Mittlere Reichweite R=', R)

#Berechnung der effektiven Länge
p0=1013
x0=2.5
x=x0*(p/p0)
print('effektive Länge=',x)

def f(x, a, b):
    return a*x+b
params, cov = curve_fit(f, x1, N1)
errors = np.sqrt(np.diag(cov))
print('a =', params[0], '±', errors[0])
print('b =', params[1], '±', errors[1])
a=ufloat(params[0], errors[0])
b=ufloat( params[1], errors[1])

#Rechnung Rm hier in cm
N2=46252.5#N/2
Rm=(N2 -b)/a
print('Rm=', Rm)
#Rm in mm
Rm=Rm*10
#Energie
Ea=(Rm/3.1)**2/3
print('Ea=', Ea)

t=np.linspace(1.23, 2.45)
#plt.plot (x, y, 'rx', label='Messwerte')
plt.plot(x,N , 'rx', label='Messwerte')
plt.plot(t,f(t, *params), 'b-' ,label='Ausgleichsgerade')
plt.axhline(y=46252.5)
plt.axvline(x=1.93)
#plt.yscale('log')
plt.xlabel(r'$ x/cm$')
plt.ylabel(r'$ N$')
plt.tight_layout()
plt.legend()
plt.savefig('plot1.pdf')
plt.show()
