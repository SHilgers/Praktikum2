import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat

a, b, c, d = np.genfromtxt('Werte1.txt', unpack=True)

def f(x, a, b):
    return a*x + b

params, cov = curve_fit(f, a, d)
errors = np.sqrt(np.diag(cov))

print('a =', params[0], '±', errors[0])
print('b =', params[1], '±', errors[1])

t=np.linspace(0, 1800)

plt.plot (a, d, 'rx', label='Messwerte')
plt.plot(t, f(t, *params), 'b-' ,label='Lineare Regression')
plt.xlabel( r'$t \:/\: \mu s$')
plt.ylabel(r'$ln(\frac{U_C}{U_0})$')
plt.legend()

plt.savefig('plot1.pdf')
