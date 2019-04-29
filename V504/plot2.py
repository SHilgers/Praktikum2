import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat

a, b= np.genfromtxt('Werte6.txt', unpack=True)

a1= np.log(a)
b1= np.log(b)
#plt.plot(t, f(t, *params), 'b-' ,label='Lineare Regression')
def f(x, a, b):
    return a*x +b


params1, cov1 = curve_fit(f, a1, b1)

covv1 = np.sqrt(np.diag(cov1))

print(params1[0],'pm',covv1[0], 'und b ist ',params1[1],'pm',covv1[1])

x=np.linspace(0, 5.7, 10000)
plt.plot (a1, b1, 'rx', label='Messwerte')

plt.plot(x,f(x, *params1), 'r-', label='Ausgleichsgerade' )

#plt.plot(x,f(x, *params), 'b-' ,label='Ausgleichsfunktion f(x)')
#plt.axhline(y=3.167131, color='slateblue', linestyle='--', label='y =\frac{1}{\sqrt2}(\frac{U_c}{U})_{\text{max}}')
#plt.axvline(x=29000, color='slateblue', linestyle='--',label='Halbwertsbreite')
#plt.axvline(x=37500 , color='slateblue', linestyle='--')
plt.grid()
plt.xlabel(r'$ln(U)$')
plt.ylabel(r'$ ln(I) $')
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('plot2.pdf')
plt.show()
