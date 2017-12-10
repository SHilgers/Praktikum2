import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat

a, b = np.genfromtxt('Werte2.txt', unpack=True)
b=b/b[0]
a=a*2*np.pi 
def f(x, b):
    return 1/(1+x**2*b)

params, cov = curve_fit(f, a, b)
errors = np.sqrt(np.diag(cov))

print('a =', params[0], '±', errors[0])
#print('b =', params[1], '±', errors[1])



t=np.linspace(9, 5000, 10000)
plt.xlim(9,5500)
plt.xscale('log')
plt.plot (a, b, 'rx', label='Messwerte')
plt.plot(t, f(t, *params), 'b-' ,label='Ausgleichsfunktion f(x)')
plt.xlabel(r'$\nu\:/\:\mathrm{Hz}$')
plt.ylabel(r'$ \frac{U_C}{U_0}$')
plt.legend()
plt.tight_layout()
plt.savefig('plot2.pdf')

g= ufloat(6.33917052388*10**(-6), 9.83577821313*10**(-7))
h= (g)**(1/2)
print(h)
