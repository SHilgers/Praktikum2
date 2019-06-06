import numpy as np
from numpy import exp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.stats import sem

swr, d, eich = np.genfromtxt('Werte2.txt', unpack=True)

x = np.linspace(0,50 ,1000)
plt.plot (d , eich,'r+', label='Theoriedaten')
plt.plot(d, swr, label='Messwerte')
#plt.plot(d, 10*np.log10(swr), label='Messwerte')

plt.grid()
plt.xlabel(r'd in mm')
plt.ylabel(r'$Dämpfung$ in dB')
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('plot1.pdf')
plt.show()
