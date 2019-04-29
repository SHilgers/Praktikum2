import numpy as np
from numpy import exp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.stats import sem

p,Emax, N = np.genfromtxt('Werte2.txt', unpack=True)
Ea, x1, N1= np.genfromtxt('Werte21.txt', unpack=True)

#Berechnung der Energien,nach linearer Skala in MeV
E0=4
E1=E0/796
E=E1*Emax
print('Energien der alpha-Teilchen=', E)

#Berechnung der effektiven Länge
p0=1013
x0=2
x=x0*(p/p0)
print('effektive Länge=',x)

def f(x, a, b):
    return a*x+b
params, cov = curve_fit(f, x1, N1)
errors = np.sqrt(np.diag(cov))
print('a =', params[0], '±', errors[0])
print('b =', params[1], '±', errors[1])
a=ufloat(params[0], errors[0])
b=ufloat(params[1], errors[1])


t=np.linspace(0.6, 8)
#plt.plot (x, y, 'rx', label='Messwerte')
plt.plot(x,N , 'rx', label='Messwerte')
#plt.plot(t,f(t, *params), 'b-' ,label='Ausgleichsgerade')
plt.axhline(y=67691)
plt.text(-0.1, 65707,'N/2')
#plt.axvline(x=7.4)
#plt.yscale('log')
plt.xlabel(r'$ x/cm$')
plt.ylabel(r'$ N$')
plt.tight_layout()
plt.legend()
plt.savefig('plot2.pdf')
plt.show()
