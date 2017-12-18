import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat

x, y = np.genfromtxt('LangeSpule.txt', unpack=True)
x=x/100
def f(x):
      return (7*4*150*np.pi*10**(-7))* (((x+0.08)/((0.0205**2 +(x+0.08)**2)**(0.5)))-((x-0.08)/(0.0205**2 +(x-0.08)**2)**(0.5)))*1000
#Faktor 6.5???
t= np.linspace(-0.14, 0.14, 1000)

plt.plot (x,y, 'rx', label='Messwerte')

plt.plot(t, f(t), 'b-', label='Theoriekurve')
#plt.plot(t, f(t, *params), 'b-' ,label='Lineare Regression')
plt.xlabel(r'Abstand vom Mittelpunkt der Spule in m')
plt.ylabel(r'B/ mT')
plt.legend()
#plt.show()
plt.savefig('LangeSpule.pdf')
