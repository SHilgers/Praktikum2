import numpy as np
from numpy import exp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat

x, y= np.genfromtxt('Werte2.txt', unpack=True)
Nu=215 #215 auf 900s
Nun=(215/900)*240
#Nun=ufloat(215/900, np.sqrt(215)/900)*10
x=x*240
dy=np.log(y)-np.log(y+np.sqrt(y))
#differenz zwischen Wert und unterem mögl. wert mit fehler
y=np.log(y-Nun)

def f(x, a, b):
    return a*x+b
params, cov = curve_fit(f, x, y)
errors = np.sqrt(np.diag(cov))
print('a =', params[0], '±', errors[0])
print('b =', params[1], '±', errors[1])
a=ufloat(params[0], errors[0])
b=ufloat( params[1], errors[1])

t=np.linspace(0, 3600)

#plt.plot (x, y, 'rx', label='Messwerte')
plt.errorbar(x, y, xerr=0, yerr=dy, fmt='o', label='Messwerte mit Fehlerbalken')
plt.plot(t,f(t, *params), 'r-' ,label='Ausgleichsgerade')
#plt.yscale('log')
plt.xlabel(r'$ t/s$')
plt.ylabel(r'$ ln(N)$')
plt.tight_layout()
plt.legend()
plt.savefig('plot2.pdf')
plt.show()
#Halbwertszeit
T=np.log(2)/a
print('T=', T)
#N0=e(b)
N0=2.718**(b)
n=2**2
print(N0)
