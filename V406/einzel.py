import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat

x,y = np.genfromtxt('Werte1.txt', unpack=True)

i=y*10**(-9)-___idunkel*10**(-9)
x=x*1000
l=635*10**(-9)
L=1.08

def f(b, z):
    return (b)**2(l/(np.pi*b*np.sin((x-z)/L)))**2*np.sin((np.pi*b*np.sin((x-z)/L))/l)

#A0??
params, cov = curve_fit(f, x, i)
errors = np.sqrt(np.diag(cov))

print('b =', params[0], '±', errors[0])
print('z =', params[1], '±', errors[1])
#print('c =', params[2], '±', errors[2])


t=np.linspace(0.20, 0.50, 100)
plt.plot (x , i, 'rx', label='Messwerte')
plt.plot(t, f(t, *params), 'b-' ,label='Ausgleichsfunktion f(x)')
plt.xlabel(r'$\text{Winkel}\;\frac{x}{L}$rad')
plt.ylabel(r'Intensität $ I $')
plt.legend()
plt.tight_layout()
plt.savefig('plot1.pdf')
