import numpy as np
from numpy import exp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat
t, a, b, c, d, p= np.genfromtxt('Werte.txt', unpack=True)

def f(t, l, m):
    return l*t+m
k=1/(d+273.15)
w=1/(c+273.15)
pa=np.log(a)
pb=np.log(b)

params, cov = curve_fit(f, k, pa)
errors = np.sqrt(np.diag(cov))
#print('ak =', params[0], '±', errors[0])
#print('bk =', params[1], '±', errors[1])

parrams, covv = curve_fit(f, w, pb)

errrors = np.sqrt(np.diag(covv))

print('aw =', parrams[0], '±', errrors[0])
print('bw =', parrams[1], '±', errrors[1])
aw=ufloat(parrams[0], errrors[0])
r=0.83144
l=-aw*r
print('L= ',l )


x=np.linspace(0, 3)
plt.xlim( 0.0030, 0.0035 )
plt.ylim( 1.5, 2.6 )
#plt.xscale('log')
#plt.plot (k, pa, 'rx', label='$T_1$')
plt.plot (w, pb, 'rx', label='$1/T_1$')
#plt.plot(x,f(x, *params), 'r-' ,label='Ausgleichsfunktion von $T_1$')
plt.plot(x,f(x, *parrams), 'r-' ,label='lineare Regression')
plt.xlabel(r'$\frac{1}{T_1} \: /\: \frac{1}{K}$')
plt.ylabel(r'$ ln{\frac{p_b}{p_0}} $')
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('plot2.pdf')
plt.show()
