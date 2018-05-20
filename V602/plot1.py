import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat

a1, b1= np.genfromtxt('a.txt', unpack=True)
a2, b2= np.genfromtxt('b.txt', unpack=True)
a3, b3= np.genfromtxt('c.txt', unpack=True)
c, d= np.genfromtxt('ka.txt', unpack=True)
f, g= np.genfromtxt('kb.txt', unpack=True)

plt.plot (a1, b1, 'r', label='Bremsberg')
plt.plot (a2, b2, 'r')
plt.plot (a3, b3, 'r')
plt.plot (c, d, 'b', label='Kα-Linie')
plt.plot (f, g, 'g', label='Kβ-Linie')


#plt.plot(x,f(x, *params), 'b-' ,label='Ausgleichsfunktion f(x)')
#plt.axhline(y=3.167131, color='slateblue', linestyle='--', label='y =\frac{1}{\sqrt2}(\frac{U_c}{U})_{\text{max}}')
#plt.axvline(x=29000, color='slateblue', linestyle='--',label='Halbwertsbreite')
#plt.axvline(x=37500 , color='slateblue', linestyle='--')
plt.grid()
plt.xlabel(r'$ \theta / °$')
plt.ylabel(r'Impulse pro s')
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('plot1.pdf')
plt.show()
