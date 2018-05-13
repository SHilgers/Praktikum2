import numpy as np
from numpy import exp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat

x,I1,I2= np.genfromtxt('Werte2.txt', unpack=True)
x=x*0.625
L=0.143
z=x/(L**(2)+x**(2))
u=1.2566*10**(-6)
n=20
R=0.282
B=(8*u*n*I1)/(R*np.sqrt(125))
B=B*10**(3)


def f(x, a, b):
    return a*x+b

#params1, cov1 = curve_fit(f, B, z)
#errors1 = np.sqrt(np.diag(cov1))

params2, cov2 = curve_fit(f, B, x)
errors2 = np.sqrt(np.diag(cov2))

#print('a1 =', params1[0], '±', errors1[0])
#print('b =', params1[1], '±', errors1[1])

print('a1 =', params2[0], '±', errors2[0])
print('b =', params2[1], '±', errors2[1])

print(B)
t=np.linspace(0, 0.2)
#plt.plot (B, z, 'rx', label='Messwerte bei U=250 V')
plt.plot (B, x, 'rx', label='Messwerte bei U=250 V')
#plt.plot(t,f(t, *params1), 'b-' ,label='Ausgleichsgerade$')
plt.plot(t,f(t, *params2), 'b-' ,label='Ausgleichsgerade')
plt.xlabel(r'$ B/\: \mathrm{mT}$')
plt.ylabel(r'$ D /\: \mathrm{cm} $')
plt.tight_layout()
plt.legend()
plt.savefig('plot4.pdf')
plt.show()
me1=((2*250)*params2**(2))/((0.08)*(L+(2))**(2))
print(me1)
