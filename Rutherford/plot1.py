import numpy as np
from numpy import exp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.stats import sem

x1, y1 = np.genfromtxt('Werte1.txt', unpack=True)
x2, y2 = np.genfromtxt('Werte2.txt', unpack=True)
def f(x, a,b):
    return a*x+b

l = np.linspace(70, 300, 50000)
params, cov = curve_fit(f, x1, y1)
covv = np.sqrt(np.diag(cov))
print('a1 ist ',params[0],'pm',covv[0])
print('b ist ',params[1],'pm',covv[1])
#print('c ist ',params[2],'pm',covv[2])
plt.plot (x1,y1 ,'kx', label='Messwerte')
#plt.plot (l, f(l, *params), 'r-', label='Fit')
#plt.errorbar(wx, wy, xerr=dx, yerr=dy  ,fmt='k.',label='Messwerte')
plt.xlabel(r'$d / cm$')
plt.ylabel(r'$ I / μA $ ')
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('plot1.pdf')
plt.show()
