import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat

a1, b1= np.genfromtxt('Werte1.txt', unpack=True)
a2, b2= np.genfromtxt('Werte2.txt', unpack=True)
a3, b3= np.genfromtxt('Werte3.txt', unpack=True)
a4, b4= np.genfromtxt('Werte4.txt', unpack=True)
a5, b5= np.genfromtxt('Werte5.txt', unpack=True)

#plt.plot(t, f(t, *params), 'b-' ,label='Lineare Regression')
def f(x, c, d, s):
    return s- c* (np.exp(-d*x))


params1, cov1 = curve_fit(f, a1, b1)
params2, cov2 = curve_fit(f, a2, b2)
params3, cov3 = curve_fit(f, a3, b3)
params4, cov4 = curve_fit(f, a4, b4)
params5, cov5 = curve_fit(f, a5, b5)

covv1 = np.sqrt(np.diag(cov1))
covv2 = np.sqrt(np.diag(cov2))
covv3 = np.sqrt(np.diag(cov3))
covv4 = np.sqrt(np.diag(cov4))
covv5 = np.sqrt(np.diag(cov5))

print(params1[2],'pm',covv1[2],params2[2],'pm',covv2[2],params3[2],'pm',covv3[2],params4[2],
'pm',covv4[2],params5[2],'pm',covv5[2])

x=np.linspace(0, 200, 10000)
plt.plot (a1, b1, 'rx', label='Messwerte 1')
plt.plot (a2, b2, 'bx', label='Messwerte 2')
plt.plot (a3, b3, 'x',color= 'lime', label='Messwerte 3')
plt.plot (a4, b4, 'x',color= 'purple', label='Messwerte 4')
plt.plot (a5, b5, 'x',color= 'orange', label='Messwerte 5')
plt.plot(x,f(x, *params1), 'r-' )
plt.plot(x,f(x, *params2), 'b-' )
plt.plot(x,f(x, *params3), '-',color= 'lime' )
plt.plot(x,f(x, *params4), '-' ,color= 'purple')
plt.plot(x,f(x, *params5), '-' ,color= 'orange')

#plt.plot(x,f(x, *params), 'b-' ,label='Ausgleichsfunktion f(x)')
#plt.axhline(y=3.167131, color='slateblue', linestyle='--', label='y =\frac{1}{\sqrt2}(\frac{U_c}{U})_{\text{max}}')
#plt.axvline(x=29000, color='slateblue', linestyle='--',label='Halbwertsbreite')
#plt.axvline(x=37500 , color='slateblue', linestyle='--')
plt.grid()
plt.xlabel(r'$U / V$')
plt.ylabel(r'$ I / mA$')
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('plot1.pdf')
plt.show()
