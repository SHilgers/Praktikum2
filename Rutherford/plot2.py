import numpy as np
from numpy import exp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.stats import sem

x1, y = np.genfromtxt('Werte3.txt', unpack=True)
def f(x, a,b):
    return a*x+b
dy=y**(0.5)
y1=y/360
dy1=dy/360
plt.errorbar(x1, y1, xerr=0, yerr=dy1  ,fmt='r.',label='Messwerte')
#plt.plot (x1,y1 ,'bx', label='Messwerte')

plt.xlabel(r'Winkel/°')
plt.ylabel(r'Counts pro s')
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('plot2.pdf')
plt.show()
