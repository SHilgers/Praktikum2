import numpy as np
from numpy import exp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.stats import sem


def f(x, a, b):
    return a*x+b

wx=[3.488, 5.735, 4.144, 0.083]

wy=[3772.356, 6336.503, 4639.166, 98.857]

#for m in range (0,11):
#    x[m]=array(wx[m],dx[m])
#    y[m]=array(wy[m],dy[m])
params, cov = curve_fit(f, wx, wy)
errors = np.sqrt(np.diag(cov))
#print('a= ',params[0],' +- ', errors[0], b= ', params[1],' +- ', errors[1])
print('a =', params[0], '±', errors[0])
print('b =', params[1], '±', errors[1])

x=np.linspace(0,6, 50000)

plt.plot (x, f(x, *params), 'r-', label='Lineare Regression')
#plt.errorbar(wx, wy, xerr=dx, yerr=dy  ,fmt='k.',label='Messwerte')
plt.plot (wx, wy, 'kx', label='Wertepaare')
plt.xlabel(r'L')
plt.ylabel(r'$ I $ ')
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('plot11.pdf')
plt.show()
