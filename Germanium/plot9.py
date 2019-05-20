import numpy as np
from numpy import exp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.stats import sem


def f(x, a, b):
    return a*x+b

wx=[0.29, 0.13, 1.6, 3.7, 10, 1.4]
dx=[0.20, 0.09, 1.1, 2.5, 7, 0.9]

dy= [20, 40, 26, 22, 40, 17]
wy=[61, 110, 1588, 3620, 10290, 1404]

#for m in range (0,11):
#    x[m]=array(wx[m],dx[m])
#    y[m]=array(wy[m],dy[m])
params, cov = curve_fit(f, wx, wy, sigma=dy, absolute_sigma=True)
errors = np.sqrt(np.diag(cov))
#print('a= ',params[0],' +- ', errors[0], b= ', params[1],' +- ', errors[1])
print('a =', params[0], '±', errors[0])
print('b =', params[1], '±', errors[1])

x=np.linspace(0,15, 50000)

plt.plot (x, f(x, *params), 'r-', label='Lineare Regression')
plt.errorbar(wx, wy, xerr=dx, yerr=dy  ,fmt='k.',label='Messwerte')
#plt.plot (wx, wy, 'kx', label='Wertepaare')
plt.xlabel(r'$L \: / \:s$')
plt.ylabel(r'$ I $ ')
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('plot9.pdf')
plt.show()
