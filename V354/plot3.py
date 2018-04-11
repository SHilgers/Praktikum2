import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat

a, b, c= np.genfromtxt('Werte6.txt', unpack=True)

d= b/c

f=4.479/np.sqrt(2)
#plt.plot(t, f(t, *params), 'b-' ,label='Lineare Regression')

plt.plot (a, d, 'rx', label='Messwerte')
#plt.plot(x,f(x, *params), 'b-' ,label='Ausgleichsfunktion f(x)')
plt.axhline(y=3.167131, color='slateblue', linestyle='--', label='y =\frac{1}{\sqrt2}(\frac{U_c}{U})_{\text{max}}')
plt.axvline(x=29000, color='slateblue', linestyle='--',label='Halbwertsbreite')
plt.axvline(x=37500 , color='slateblue', linestyle='--')
plt.grid()
plt.xlabel(r'$\nu / hz$')
plt.ylabel(r'$ \frac{U_c}{U}$')
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('plot3.pdf')
plt.show()
