import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat

a, b, c, d = np.genfromtxt('Werte8.txt', unpack=True)
a=a/242
def f(x):
    return np.sqrt((x**2 -1)**2)
def g(x):
    return (3*((1-(x**2))**2 + 9*(x**2))**0.5)

def h(x,y):
    return x/y



x=np.linspace(0.01, 100, 10000)
plt.xscale('log')
plt.plot (a, d, 'rx', label='Messwerte')
plt.plot(x,h(f(x),g(x)), 'b-' ,label='Ausgleichsfunktion f(x)')
#plt.plot(x, np.sqrt(((x**2-1)**2)/(((1-x**2)**2+9*x**2)*9)))
plt.xlabel(r'$\frac{\nu}{\nu_0}$')
plt.ylabel(r'$ \frac{U_b}{U_s}$')
plt.legend(loc="lower right")
plt.tight_layout()
plt.savefig('plot.pdf')
plt.show()
