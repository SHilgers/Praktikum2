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
x1=x1*100
x2=x2*100
l1 = np.linspace(7000, 28000, 50000)
l2 = np.linspace(7000, 21000, 50000)
params, cov = curve_fit(f, x1[6:], y1[6:])
covv = np.sqrt(np.diag(cov))
print('a1 ist ',params[0],'pm',covv[0])
print('b1 ist ',params[1],'pm',covv[1])
params2, cov2 = curve_fit(f, x2, y2)
covv2 = np.sqrt(np.diag(cov2))
print('a2 ist ',params2[0],'pm',covv2[0])
print('b2 ist ',params2[1],'pm',covv2[1])
#print('c ist ',params[2],'pm',covv[2])
plt.plot (x1,y1 ,'bx', label='Messwerte ohne Folie')
plt.plot (x2,y2 ,'rx', label='Messwerte mit Folie')

plt.plot (l1, f(l1, *params), 'b-', label='Lineare Ausgleichsgerade ohne Folie')
plt.plot (l2, f(l2, *params2), 'r-', label='Lineare Ausgleichsgerade mit Folie')
#plt.errorbar(wx, wy, xerr=dx, yerr=dy  ,fmt='k.',label='Messwerte')
plt.xlabel(r'$p / Pa$')
plt.ylabel(r'$ U / V $ ')
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('plot1.pdf')
b1= ufloat(params[1],covv[1])
b2= ufloat(params2[1],covv2[1])
b3=b1-b2
print(b3)
E=5.638*b3/b1
print(E)
plt.show()
