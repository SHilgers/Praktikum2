import numpy as np
from numpy import exp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.stats import sem

a, b, c, d= np.genfromtxt('Werte2.txt', unpack=True)

def f(x, a, b):
    return a*x +b

vh = np.log(b/a)
c2= 2*c
params, cov = curve_fit(f, c2, vh)
errors = np.sqrt(np.diag(cov))
print('a =', params[0], '±', errors[0])
print('b =', params[1], '±', errors[1])

t = np.linspace(0,250)
plt.plot (c2, vh, 'rx', label='Messwerte')
plt.plot(t,f(t, *params), 'b-' ,label='Ausgleichsgerade ')
plt.xlabel(r'$ 2 \cdot l / mm $')
plt.ylabel(r'$ ln(U_{0}/U_{1})$')
plt.tight_layout()
plt.legend()
plt.savefig('plot1.pdf')
plt.show()
