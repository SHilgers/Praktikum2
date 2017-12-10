import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat

a, b, c, d = np.genfromtxt('Werte8.txt', unpack=True)
a=a/242
def f(x):
    return (((x**2)-1)**2)/((((1-x**2)**2)+9*x**2)*9)



t=np.linspace(0.01, 1000)
plt.xscale('log')
#plt.plot (a, d, 'rx', label='Messwerte')
plt.plot(t, np.sqrt(f(t)), 'b-' ,label='Ausgleichsfunktion f(x)')
plt.xlabel(r'$\nu\:/\:\mathrm{Hz}$')
plt.ylabel(r'$ \frac{U_C}{U_0}$')
plt.legend()
plt.tight_layout()
plt.savefig('plot.pdf')
plt.show()
