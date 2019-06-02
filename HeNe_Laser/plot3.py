import numpy as np
from numpy import exp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.stats import sem

x, y = np.genfromtxt('Werte3.txt', unpack=True)

def f(x,a, b, c):
    return a*np.exp(-((x-b)**2/(c**2)))
l = np.linspace(0, 45, 50000)
params, cov = curve_fit(f, x, y)
covv = np.sqrt(np.diag(cov))

print('a =', params[0], '±', covv[0])
print('b =', params[1], '±', covv[1])
print('c =', params[2], '±', covv[2])
plt.plot (x,y ,'kx', label='Messwerte')
plt.plot (l, f(l, params[0], params[1], params[2]), 'r-', label='Fit')
#plt.errorbar(wx, wy, xerr=dx, yerr=dy  ,fmt='k.',label='Messwerte')
plt.xlabel(r'x \ mm')
plt.ylabel(r'$ I \ μA$ ')
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('plot3.pdf')
plt.show()
