import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat

x, y = np.genfromtxt('KurzeSpule.txt', unpack=True)
x=x/100
def f(x):
      return (10*0.5*4*1700*np.pi*10**(-7))* (((x+0.05)/((0.05**2 +(x+0.05)**2)**(0.5)))-((x-0.05)/(0.05**2 +(x-0.05)**2)**(0.5)))*1000
#Faktor 10??????

t= np.linspace(-0.11, 0.11)

plt.plot (x,y, 'rx', label='Messwerte')
plt.plot(t, f(t), 'b-', label='Theoriekurve')

plt.xlabel(r'Abstand vom Mittelpunkt der Spule in m')
plt.ylabel(r'B/ mT')
plt.legend()

plt.savefig('KurzeSpule.pdf')
