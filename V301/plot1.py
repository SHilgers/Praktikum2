import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat

y, x = np.genfromtxt('werte1.txt', unpack=True)


def f(x, a, b):
    return a*x - b

params, cov = curve_fit(f, x, y)
errors = np.sqrt(np.diag(cov))
#print('a= ',params[0],' +- ', errors[0],
#'& b= ', params[1],' +- ', errors[1])
print('a =', params[0], '±', errors[0])
print('b =', params[1], '±', errors[1])

t= np.linspace(15, 95)

plt.plot (x,y, 'rx', label='Messwerte')
plt.plot(t, f(t, *params), 'b-' ,label='Lineare Regression')
plt.ylabel(r'$ U_{k} \: \mathrm{volt}$')
plt.xlabel (r'$I \: \mathrm{mA} $')
plt.legend ()
plt.savefig('plot1.pdf')
