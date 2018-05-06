import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat

a, b= np.genfromtxt('Werte7.txt', unpack=True)
c=np.log(b)
#plt.plot(t, f(t, *params), 'b-' ,label='Lineare Regression')
def f(x, a, b):
    return a*x +b
params1, cov1 = curve_fit(f, a, c)

covv1 = np.sqrt(np.diag(cov1))

print(params1[0],'pm',covv1[0], 'und b ist ',params1[1],'pm',covv1[1])
k =ufloat(params1[0],covv1[0])
t= (1.602*10**(-19))/(1.3806*10**(-23)*k)
print('T= ',t)
x=np.linspace(0, 1, 10000)
plt.plot(x,f(x, *params1), 'r-', label='Ausgleichsgerade' )

plt.plot (a, c, 'rx', label='Messwerte')

plt.grid()
plt.xlabel(r'$U / V$')
plt.ylabel(r'$ ln(I) $')
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('plot3.pdf')
plt.show()
