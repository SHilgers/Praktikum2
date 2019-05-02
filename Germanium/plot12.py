import numpy as np
from numpy import exp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.stats import sem


def f(x, a, b):
    return a*x+b

wx=[0.126, 0.341, 0.072, 0.171, 0.657, 0.069, 0.226, 0.134,
0.079, 0.064, 0.028, 0.072, 0.375, 0.047, 0.089]

wy=[153.501, 407.572, 88.821, 216.897, 923.364, 108.785,
354.664, 188.872, 88.562, 80.894, 64.034, 137.768, 704.686,
99.247, 173.018]


#for m in range (0,11):
#    x[m]=array(wx[m],dx[m])
#    y[m]=array(wy[m],dy[m])
params, cov = curve_fit(f, wx, wy)
errors = np.sqrt(np.diag(cov))
#print('a= ',params[0],' +- ', errors[0], b= ', params[1],' +- ', errors[1])
print('a =', params[0], '±', errors[0])
print('b =', params[1], '±', errors[1])

x=np.linspace(0,1, 50000)

plt.plot (x, f(x, *params), 'r-', label='Lineare Regression')
#plt.errorbar(wx, wy, xerr=dx, yerr=dy  ,fmt='k.',label='Messwerte')
plt.plot (wx, wy, 'kx', label='Wertepaare')
plt.xlabel(r'L')
plt.ylabel(r'$ I $ ')
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('plot12.pdf')
plt.show()
