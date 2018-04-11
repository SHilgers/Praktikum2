import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat

x, y = np.genfromtxt('Helmholz1.txt', unpack=True)
x=x/100

def g(x):
    return ((4*np.pi*10**(-7)*2*0.0625**2)/(0.0625**2+ (x)**2)**(3/2))*200*1000

t= np.linspace(0.06, 0.26, 1000)

plt.plot (x,y, 'rx', label='Messwerte')
#plt.plot(x, (np.pi*10**(-7)*2*0.0625**2)/(0.0625**2+ x**2)**(5/2)*10)
plt.plot(t, g(t), 'b-', label='Theoriekurve')
plt.xlabel(r'Abstand vom Spule 1 in m')
plt.ylabel(r'B/ mT')
plt.legend()
plt.savefig('Helmholz1.pdf')
