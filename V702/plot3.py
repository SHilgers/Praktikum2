import numpy as np
from numpy import exp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat

x, y= np.genfromtxt('Werte1.txt', unpack=True)
Nu=215 #215 auf 900s
Nun=(215/900)*10
#Nun=ufloat(215/900, np.sqrt(215)/900)*10
x=x*10
dy=np.log(y)-np.log(y+np.sqrt(y))
#differenz zwischen Wert und unterem mögl. wert mit fehler
y=np.log(y-Nun)


t=np.linspace(0, 450)

#plt.plot (x, y, 'rx', label='Messwerte')
plt.errorbar(x, y, xerr=0, yerr=dy, fmt='o', label='Messwerte mit Fehlerbalken')

#plt.yscale('log')
plt.xlabel(r'$ t/s$')
plt.ylabel(r'$ ln(N)$')
plt.tight_layout()
plt.legend()
plt.savefig('plot3.pdf')
plt.show()
