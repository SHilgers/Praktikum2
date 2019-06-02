import numpy as np
from numpy import exp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.stats import sem

x, y = np.genfromtxt('Werte1.txt', unpack=True)

def f(x, a,b):
    return a*(x**2/b**2-x*2/b+1)

l = np.linspace(70, 132, 50000)
params, cov = curve_fit(f, x[0:24], y[0:24], p0=(400, 100))
covv = np.sqrt(np.diag(cov))
print('a1 ist ',params[0],'pm',covv[0])
print('b ist ',params[1],'pm',covv[1])
#print('c ist ',params[2],'pm',covv[2])
plt.plot (x,y ,'kx', label='Messwerte')
plt.plot (l, f(l, *params), 'r-', label='Fit')
#plt.errorbar(wx, wy, xerr=dx, yerr=dy  ,fmt='k.',label='Messwerte')
plt.xlabel(r'$d / cm$')
plt.ylabel(r'$ I / μA $ ')
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('plot1.pdf')
plt.show()
