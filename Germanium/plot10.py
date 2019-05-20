import numpy as np
from numpy import exp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.stats import sem

acs = np.genfromtxt('Caesium.txt', unpack=True)
bc = np.linspace(1, 8191, 8192)
bcs=bc*0.403169-3.034
Ecae = (661.5985+3.034)/0.403169
eps = Ecae/((510.998946+3.034)/0.403169)
def f(x, b):
    return b*(1/eps**2)*(2+(Ecae/(x-Ecae))**2+((1/eps**2)+((x-Ecae)/x)-2/eps*((x-Ecae)/x)))
x = np.linspace(50, 1050, 50000)
params4, cov = curve_fit(f, bc[553:1049], acs[553:1049])
covv4 = np.sqrt(np.diag(cov))
print('a1 ist ',params4,'pm',covv4)
plt.plot (bc[0:1050], acs[0:1050], 'k-', label='Messwerte')
plt.plot (x, f(x, 6.77907707), 'r-', label='Fit')
#plt.errorbar(wx, wy, xerr=dx, yerr=dy  ,fmt='k.',label='Messwerte')
plt.xlabel(r'L')
plt.ylabel(r'$ I $ ')
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('plot10.pdf')
plt.show()
