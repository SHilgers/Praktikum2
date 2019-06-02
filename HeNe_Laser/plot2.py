import numpy as np
from numpy import exp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.stats import sem

x, y = np.genfromtxt('Werte2.txt', unpack=True)

def f(x,a, b):
    return a*(1-x/b)
l = np.linspace(60, 96, 50000)
params, cov = curve_fit(f, x, y)
covv = np.sqrt(np.diag(cov))
print('a ist ',params[0],'pm',covv[0])
print('b ist ',params[1],'pm',covv[1])
plt.plot (x,y ,'kx', label='Messwerte')
plt.plot (l, f(l, *params), 'r-', label='Fit')
#plt.errorbar(wx, wy, xerr=dx, yerr=dy  ,fmt='k.',label='Messwerte')
plt.xlabel(r'd / cm')
plt.ylabel(r'$ I / μA $ ')
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('plot2.pdf')
plt.show()
