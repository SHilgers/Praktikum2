import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat

a, b, c= np.genfromtxt('Werte3.txt', unpack=True)
d= b/c * 2* np.pi
def f(x, a):
    return np.arctan(a*(x))

params, cov = curve_fit(f, a, d)
errors = np.sqrt(np.diag(cov))

print('a =', params[0], '±', errors[0])
#print('b =', params[1], '±', errors[1])
#print('c =', params[2], '±', errors[2])


t=np.linspace(9, 5000, 10000)
plt.xlim(9,5500)
plt.xscale('log')
plt.yticks( [0, np.pi/4, np.pi/2],[ r'$0$', r'$\pi/4$',r'$\pi/2$'])
plt.plot (a, d, 'rx', label='Messwerte')
plt.plot(t, f(t, *params), 'b-' ,label='Ausgleichsfunktion f(x)')
plt.xlabel(r'$\nu\:/\:\mathrm{Hertz}$')
plt.ylabel(r'$ \phi \: / \:$ rad')
plt.legend()
plt.tight_layout()
plt.savefig('plot3.pdf')
