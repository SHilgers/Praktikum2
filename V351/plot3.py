import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat

y, x = np.genfromtxt('WerteSäage.txt', unpack=True)
x =np.log(x)
y =np.log(y)
def f(x, a, b):
    return a*x + b

params, cov = curve_fit(f, x, y)
errors = np.sqrt(np.diag(cov))
#print('a= ',params[0],' +- ', errors[0], b= ', params[1],' +- ', errors[1])
print('a =', params[0], '±', errors[0])
print('b =', params[1], '±', errors[1])
t= np.linspace(-2.5, 0)

plt.plot (x,y, 'rx', label='Messwerte')
plt.plot(t, f(t, *params), 'b-' ,label='Lineare Regression')
plt.xlabel(r'Logarithmus der Nummer der Oberwelle')
plt.ylabel(r'$log(\frac{U_{n}}{U_{1}})$')
plt.legend()
#plt.show()
#plt.yscale('log')
#plt.xscale('log')
plt.savefig('plot3.pdf')
