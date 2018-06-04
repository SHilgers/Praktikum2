import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat

a, b, c, d, f= np.genfromtxt('Werte1.txt', unpack=True)
a2, b2, c2, d2, f2= np.genfromtxt('Werrte2.txt', unpack=True)

def f(x, a, b):
    return a*x +b


params1, cov1 = curve_fit(f, a2, b2)

covv1 = np.sqrt(np.diag(cov1))

print(params1[0],'pm',covv1[0], 'und b ist ',params1[1],'pm',covv1[1])
errX = c
x=np.linspace(400, 650)
#plt.plot (a, b, 'rx', label='Messwerte')
plt.errorbar(a, b, xerr=0, yerr=c  ,fmt='o',label='Messwerte')

plt.plot(x,f(x, *params1), 'r-', label='Ausgleichsgerade' )

#plt.plot(x,f(x, *params), 'b-' ,label='Ausgleichsfunktion f(x)')
#plt.axhline(y=3.167131, color='slateblue', linestyle='--', label='y =\frac{1}{\sqrt2}(\frac{U_c}{U})_{\text{max}}')
#plt.axvline(x=29000, color='slateblue', linestyle='--',label='Halbwertsbreite')
#plt.axvline(x=37500 , color='slateblue', linestyle='--')
plt.grid()
plt.xlabel(r'$U/V$')
plt.ylabel(r'$N \: \: pro \: \: min$')
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('plot1.pdf')
plt.show()
