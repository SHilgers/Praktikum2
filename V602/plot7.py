import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat

e0= 1.602176462*10**(-19)
a, b= np.genfromtxt('Mos.txt', unpack=True)
#b=b*e0
b=(b)**(1/2)
def f(x, a, b):
    return a*x+b

params1, cov1 = curve_fit(f, a, b)
covv1 = np.sqrt(np.diag(cov1))
print(params1[0],'pm',covv1[0],params1[1],'pm',covv1[1])
x=np.linspace(0, 40, 10000)
plt.plot (a, b, 'rx', label='Messwerte')
plt.plot(x,f(x, *params1), 'r-', label='Ausgleichsgerade' )


#plt.plot(x,f(x, *params), 'b-' ,label='Ausgleichsfunktion f(x)')
#plt.axhline(y=3.167131, color='slateblue', linestyle='--', label='y =\frac{1}{\sqrt2}(\frac{U_c}{U})_{\text{max}}')
#plt.axvline(x=29000, color='slateblue', linestyle='--',label='Halbwertsbreite')
#plt.axvline(x=37500 , color='slateblue', linestyle='--')
plt.grid()
plt.xlabel(r'$ Z $')
plt.ylabel(r'$\sqrt{E_k} / \sqrt{eV}$')
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('plot7.pdf')
plt.show()
