import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat

x, y = np.genfromtxt('Helmholz2I.txt', unpack=True)
x=x/100

def g(x):
    return ((5*4*np.pi*10**(-7)*0.0625**2)/(0.0625**2+ (x+0.00312)**2)**(3/2))*200*100

t= np.linspace(0.007, 0.0175, 1000)

plt.plot (x,y, 'rx', label='Messwerte')
plt.plot(t, g(t), 'b-', label='Theoriekurve')
#plt.plot(t, f(t, *params), 'b-' ,label='Lineare Regression')
plt.xlabel(r'Abstand von der Spule 1 in der Einheit m')
plt.ylabel(r'B/ mT')
plt.legend()
#plt.show()
#plt.yscale('log')
#plt.xscale('log')
plt.savefig('Helmholz2I.pdf')
