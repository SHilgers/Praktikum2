import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat

a, b = np.genfromtxt('Werte2.txt', unpack=True)
b = b / b[0]
def f(x, a, b, c):
    return a*np.arctan(-b*x)+c

params, cov = curve_fit(f, a, b)
errors = np.sqrt(np.diag(cov))

print('a =', params[0], '±', errors[0])
print('b =', params[1], '±', errors[1])
print('c =', params[2], '±', errors[2])


t=np.linspace(9, 5000, 10000)
plt.xlim(9,5500)
plt.xscale('log')
plt.plot (a, b, 'rx', label='Messwerte')
plt.plot(t, f(t, *params), 'b-' ,label='Ausgleichsfunktion f(x)')
plt.xlabel(r'$\nu\:/\:\mathrm{Hertz}$')
plt.ylabel(r'$ln(\frac{U_C}{U_0})$')
plt.legend()
plt.tight_layout()
plt.savefig('plot2.pdf')
