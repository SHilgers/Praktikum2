import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat

a, b, c= np.genfromtxt('Werte3.txt', unpack=True)
d= b/c * 2* np.pi

f, g = np.genfromtxt('Werte2.txt', unpack=True)
g=g/g[0]

def A(f, phi):
    return -np.sin(phi)/f

polar_plot = np.linspace(0.0000000001, np.pi/2, 100000)
plt.polar(d, g, 'rx', label='Messwerte')
plt.polar(polar_plot, A(-np.tan(polar_plot), polar_plot), label='Theorie')
plt.legend(loc='best')
plt.xticks( [0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi, 5*np.pi/4, 3*np.pi/2,
7*np.pi/4],[ r'$0$', r'$\pi/4$',r'$\pi/2$', r'$3\pi/4$',
r'$\pi$', r'$5\pi/4$', r'$3\pi/2$', r'$7\pi/4$'])
plt.savefig('plot4.pdf')
plt.show()
