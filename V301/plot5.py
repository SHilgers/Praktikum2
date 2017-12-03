import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat

y, x = np.genfromtxt('werte5.txt', unpack=True)


def f(x, a, b):
    return (a**2/(x+b)**2)*x

params, cov = curve_fit(f, x, y)
errors = np.sqrt(np.diag(cov))
#print('a= ',params[0],' +- ', errors[0],
#'& b= ', params[1],' +- ', errors[1])
print('a =', params[0], '±', errors[0])
print('b =', params[1], '±', errors[1])

t= np.linspace(0, 100)

plt.plot (x,y, 'rx', label='Messwerte')
plt.plot(t, f(t, *params), 'b-' ,label='Theoriekurve')
plt.ylabel(r'$ N\:/ W*10^-3$')
plt.xlabel (r'$R_{a}\: /\Omega$')
plt.legend ()
plt.savefig('plot5.pdf')
