import numpy as np
from numpy import exp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat

x,y1, y2 = np.genfromtxt('Werte2.txt', unpack=True)
x=x*0.625
#z=y/x

def f(x,a,b):
    return a*x+b

params1, cov1 = curve_fit(f, x, y1)
errors1 = np.sqrt(np.diag(cov1))
print('a1 =', params1[0], '±', errors1[0])
print('b1 =', params1[1], '±', errors1[1])

params2, cov2 = curve_fit(f, x, y2)
errors2 = np.sqrt(np.diag(cov2))
print('a2 =', params2[0], '±', errors2[0])
print('b2 =', params2[1], '±', errors2[1])


t=np.linspace(0, 6)
#plt.xscale('log')
plt.plot (x, y1, 'rx', label='Messwerte')
plt.plot (x, y2, 'bx', label='Messwerte')
plt.plot(t,f(t, *params1), 'r-' ,label='Ausgleichsgerade')
plt.plot(t,f(t, *params2), 'b-' ,label='Ausgleichsgerade')
plt.xlabel(r'$ U_d$')
plt.ylabel(r'$ D $')
plt.tight_layout()
plt.savefig('plot2.pdf')
plt.show()
