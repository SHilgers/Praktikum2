import numpy as np
from numpy import exp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat
t, a, b, c, d, p= np.genfromtxt('Werte.txt', unpack=True)

def f(t, l, m, n):
    return l*t**2 + m*t + n

params, cov = curve_fit(f, t, c)

errors = np.sqrt(np.diag(cov))

print('l =', params[0], '±', errors[0])
print('m =', params[1], '±', errors[1])
print('n =', params[2], '±', errors[2])

parrams, covv = curve_fit(f, t, d)

errrors = np.sqrt(np.diag(covv))

print('lk =', parrams[0], '±', errrors[0])
print('mk =', parrams[1], '±', errrors[1])
print('nk =', parrams[2], '±', errrors[2])

lw=ufloat(params[0], errors[0])
lk=ufloat(parrams[0], errrors[0])
mw=ufloat(params[1], errors[1])
mk=ufloat(parrams[1], errrors[1])

dw1 = lw*480 + mw
dw2 = lw*960 + mw
dw3 = lw*1500 + mw
dw4 = lw*1980 + mw

dk1 = lk*480 + mk
dk2 = lk*960 + mk
dk3 = lk*1500 + mk
dk4 = lk*1980 + mk

print ('dw= ', dw1, dw2, dw3, dw4)
print ('dk= ', dk1, dk2, dk3, dk4)


x=np.linspace(0, 2000)
#plt.xscale('log')
plt.plot (t, c, 'rx', label='$T_1$')
plt.plot (t, d, 'bx', label='$T_2$')
plt.plot(x,f(x, *params), 'r-' ,label='Ausgleichsfunktion von $T_1$')
plt.plot(x,f(x, *parrams), 'b-' ,label='Ausgleichsfunktion von $T_2$')
plt.xlabel(r'$t \: /\: s$')
plt.ylabel(r'$ T \: / \: °C $')
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('plot1.pdf')
plt.show()
