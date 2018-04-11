import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat

a, b, h= np.genfromtxt('Werte4.txt', unpack=True)
c=1000000/a

d= b/c * 2* np.pi
#def f(x, a):
    #return np.arctan(a*(x))
print(d)
#params, cov = curve_fit(f, a, d)
#errors = np.sqrt(np.diag(cov))

#print('a =', params[0], '±', errors[0])
#print('b =', params[1], '±', errors[1])
#print('c =', params[2], '±', errors[2])


t=np.linspace(9, 5000, 10000)
#plt.xlim(9,5500)
plt.xscale('log')
plt.yticks( [0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi],[ r'$0$', r'$\pi/4$', r'$\pi/2$', r'$3/4\pi$', r'$\pi$'])
plt.plot (a, d, 'rx', label='Messwerte')
#plt.plot(t, f(t, *params), 'b-' ,label='Ausgleichsfunktion f(x)')
plt.xlabel(r'$\nu\:/\:\mathrm{Hertz}$')
plt.ylabel(r'$ \phi \: / \:$ rad')
plt.legend()
plt.tight_layout()
plt.savefig('plot4.pdf')
plt.show()
