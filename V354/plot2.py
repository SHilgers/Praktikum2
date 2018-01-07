import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat

a, b, c= np.genfromtxt('Werte3.txt', unpack=True)

d= b/c
minVal, maxVal = None, None
list = d
for item in list:
 if minVal == None or item < minVal:
     minVal = item
 if maxVal == None or item > maxVal:
     maxVal = item
print ("Die kleinste Zahl ist %s und die groesste Zahl ist %s." % (minVal, maxVal))


#plt.plot(t, f(t, *params), 'b-' ,label='Lineare Regression')



plt.xscale('log')
plt.plot (a, d, 'rx', label='Messwerte')
#plt.plot(x,f(x, *params), 'b-' ,label='Ausgleichsfunktion f(x)')

plt.xlabel(r'$\nu / hz$')
plt.ylabel(r'$ \frac{U_c}{U}$')
plt.legend(loc="upper left")
plt.tight_layout()
plt.savefig('plot2.pdf')
plt.show()
