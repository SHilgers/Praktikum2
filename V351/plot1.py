import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
#from uncertainties import ufloat

y, x = np.genfromtxt('WerteRechteck.txt', unpack=True)
x = x*10**(3)



plt.plot (x,y, 'rx', label='Messwerte')
#plt.show()
plt.yscale('log')
plt.savefig('plot1.pdf')
