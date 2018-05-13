import numpy as np
from numpy import exp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat

x,y= np.genfromtxt('Werte3.txt', unpack=True)
x=1/x
p=0.019
L= 0.143
d=0.0038
k=(p*L)/(2*d)
def f(x, a, b):
    return a*x+b

params1, cov1 = curve_fit(f, x, y)
errors1 = np.sqrt(np.diag(cov1))

print('a1 =', params1[0], '±', errors1[0])
print('b =', params1[1], '±', errors1[1])
print(k)
t=np.linspace(0.0015, 0.007)
plt.plot (x, y, 'rx', label='Messwerte')
plt.plot(t,f(t, *params1), 'b-' ,label='Ausgleichsgerade')
plt.xlabel(r'$ 1/U_B/\: \mathrm{1/V}$')
plt.ylabel(r'$ D/U_d /\: \mathrm{cm/V} $')
plt.tight_layout()
plt.legend()
plt.savefig('plot3.pdf')
plt.show()
