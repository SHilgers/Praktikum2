import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat

x, y= np.genfromtxt('Hysterese.txt', unpack=True)
#def f(x, a, b):
#    return a*x + b

#params, cov = curve_fit(f, x, y)
#errors = np.sqrt(np.diag(cov))

#print('a =', params[0], '±', errors[0])
#print('b =', params[1], '±', errors[1])
t= np.linspace(-11, 11)

plt.plot (x,y, 'rx', label='Messwerte')
#plt.plot(t, f(t, *params), 'b-' ,label='Lineare Regression')
plt.xlabel(r'I/ A')
plt.ylabel(r'B/ mT')
plt.legend()
plt.grid()
#plt.show()
plt.savefig('plothys.pdf')
