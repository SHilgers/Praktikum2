import numpy as np
from numpy import exp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.stats import sem


def f(x, a, b):
    return a*x+b

wx=[309.7021,614.649, 861.5933, 1027.214, 1108.725,
1939.357, 2158.45, 2398.828, 2700.81, 2765.961, 3500.35]
dx=[0.0050, 0.017, 0.0046, 0.061, 0.062, 0.051, 0.13,
0.086, 0.14, 0.089, 0.12]
wy=[121.7817, 244.6974, 344.2785, 411.1165, 443.965,
778.9045, 867.380, 964.079, 1085.837, 1112.076, 1408.013]
dy=[0.0003, 0.0008, 0.0012, 0.0012, 0.003, 0.0024,
0.003, 0.018, 0.010, 0.003, 0.003]#

#for m in range (0,11):
#    x[m]=array(wx[m],dx[m])
#    y[m]=array(wy[m],dy[m])
params, cov = curve_fit(f, wx, wy)
errors = np.sqrt(np.diag(cov))
#print('a= ',params[0],' +- ', errors[0], b= ', params[1],' +- ', errors[1])
print('a =', params[0], '±', errors[0])
print('b =', params[1], '±', errors[1])

x=np.linspace(0,4000, 50000)

plt.plot (x, f(x, *params), 'r-', label='Lineare Regression')
#plt.errorbar(wx, wy, xerr=dx, yerr=dy  ,fmt='k.',label='Messwerte')
plt.plot (wx, wy, 'kx', label='Messwerte')
plt.xlabel(r'Kanalnummer')
plt.ylabel(r'$ Q(E_{γ})/\si{\kilo\electronvolt}$ ')
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('plot3.pdf')
plt.show()
