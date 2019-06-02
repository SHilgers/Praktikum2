import numpy as np
import math as mt
from numpy import exp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.stats import sem

x, y = np.genfromtxt('Werte5.txt', unpack=True)
r =np.linspace(0, 37, 37)
for m in range (0,37):
    r[m] = 2*np.pi*m/36

def f(x,a,b):
    return a*(np.cos(x-b))**2


l = np.linspace(0, 360, 50000)
xl =l*2*np.pi/360

params, cov = curve_fit(f, r, y)
covv = np.sqrt(np.diag(cov))

print('a =', params[0], '±', covv[0])
print('b =', params[1], '±', covv[1])

plt.plot (x,y ,'kx', label='Messwerte')
plt.plot (l, f(xl, params[0], params[1]), 'r-', label='Fit')
plt.xlabel(r'Θ / °')
plt.ylabel(r'$ I / μA$ ')
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('plot5.pdf')
plt.show()
