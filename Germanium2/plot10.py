import numpy as np
from numpy import exp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.stats import sem

acs = np.genfromtxt('Caesium.txt', unpack=True)
bc = np.linspace(1, 8191, 8192)
bcs=bc*0.403169-3.034
Ecae = 661.5985
eps = Ecae/(510.998946)
def f(x, b):
    return b*(2+(Ecae/(x-Ecae))**2+((1/eps**2)+((x-Ecae)/x)-2/eps*((x-Ecae)/x)))
x = np.linspace(20, 478, 50000)
#params, cov = curve_fit(f, bcs[100:1198], acs[100:1198])
#covv = np.sqrt(np.diag(cov))
#print('a1 ist ',params4,'pm',covv4)
plt.plot (bcs[:2000], acs[0:2000], 'k-', label='Messwerte')
plt.plot (x, f(x,4.29702205), 'r-', label='Fit')
#plt.errorbar(wx, wy, xerr=dx, yerr=dy  ,fmt='k.',label='Messwerte')
plt.xlabel(r'L')
plt.ylabel(r'$ I $ ')
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('plot10.pdf')
plt.show()
