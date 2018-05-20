import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat

a, b= np.genfromtxt('MessungZirkonium.txt', unpack=True)

plt.plot (a, b, 'r', label='Messwerte')



#plt.plot(x,f(x, *params), 'b-' ,label='Ausgleichsfunktion f(x)')
#plt.axhline(y=3.167131, color='slateblue', linestyle='--', label='y =\frac{1}{\sqrt2}(\frac{U_c}{U})_{\text{max}}')
#plt.axvline(x=29000, color='slateblue', linestyle='--',label='Halbwertsbreite')
#plt.axvline(x=37500 , color='slateblue', linestyle='--')
plt.grid()
plt.xlabel(r'$ \theta / °$')
plt.ylabel(r'Impulse pro s')
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('Zirkonium.pdf')
plt.show()
