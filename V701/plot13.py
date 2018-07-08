import numpy as np
from numpy import exp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.stats import sem

x, N, E= np.genfromtxt('Werte13.txt', unpack=True)

def f(x, a, b):
    return a*x+b
params, cov = curve_fit(f, x, E)
errors = np.sqrt(np.diag(cov))
print('a =', params[0], '±', errors[0])
print('b =', params[1], '±', errors[1])
a=ufloat(params[0], errors[0])
b=ufloat(params[1], errors[1])


t=np.linspace(0, 2)
#plt.plot (x, y, 'rx', label='Messwerte')
plt.plot(x,E , 'rx', label='Berechnete Energiewerte')
plt.plot(t,f(t, *params), 'b-' ,label='Ausgleichsgerade')
#plt.yscale('log')
plt.xlabel(r'$ x/cm$')
plt.ylabel(r'$ E/MeV$')
plt.tight_layout()
plt.legend()
plt.savefig('plot13.pdf')
plt.show()
