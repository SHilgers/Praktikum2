import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat

x, y = np.genfromtxt('Helmholz1I.txt', unpack=True)
x=x/1000
def g(x):
    return ((4*np.pi*10**(-7)*2*0.0625**2)/(0.0625**2+ (x+0.0312)**2)**(3/2))*200*1000

t= np.linspace(0.0008 , 0.0018, 1000)

plt.plot (x,y, 'rx', label='Messwerte')
plt.plot(t,g(t) ,'-b', label='Theoriekurve')
#plt.plot(t, f(t, *params), 'b-' ,label='Lineare Regression')
plt.xlabel(r'Abstand von der Spule 1 in der Einheit $\mathrm{10m}$')
plt.ylabel(r'B/ mT')
plt.legend()
#plt.show()
#plt.yscale('log')
#plt.xscale('log')
plt.savefig('Helmholz1I.pdf')
