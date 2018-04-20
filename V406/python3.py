import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat

x,y = np.genfromtxt('Werte3.txt', unpack=True)

y=y*10**(-9)-0.1*10**(-9)
x=x/1000
l=635*10**(-9)
L=1.085


def f(x, b, m):
   return (b)**2*(l/(np.pi*b*np.sin((x-m)/L)))**2*((np.sin(np.pi*b*np.sin((x-m)/L)))/l)**(2)
#def f(x, b, m):
#    return b**(2)*(np.sinc(b*np.sin((x-m)/L))/l)**(2)

params, cov = curve_fit(f, x, y, p0=(0.000015, 0.25))
#p0=(0.000015, 0.25)
errors = np.sqrt(np.diag(cov))

print('b =', params[0], '±', errors[0])
print('m =', params[1], '±', errors[1])
#print('c =', params[2], '±', errors[2])


t=np.linspace(-0.5, 0.5, 10000)
plt.plot (x , y, 'rx', label='Messwerte')
plt.plot(t, f(t, *params), 'b-' ,label='Ausgleichsfunktion f(x)')
#plt.xlabel(r'$\text{Winkel}\;\frac{x}{L}$rad')
#plt.ylabel(r'Intensität $ I $')
plt.legend()
plt.tight_layout()
plt.show()
plt.savefig('plot3.pdf')
