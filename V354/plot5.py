import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat

a, b= np.genfromtxt('Werte5.txt', unpack=True)
c=1000000/a

d= b/c * 2* np.pi
#def f(x, a):
    #return np.arctan(a*(x))
#print(d)
#params, cov = curve_fit(f, a, d)
#errors = np.sqrt(np.diag(cov))

#print('a =', params[0], '±', errors[0])
#print('b =', params[1], '±', errors[1])
#print('c =', params[2], '±', errors[2])


t=np.linspace(9, 5000, 10000)
plt.axhline(y=np.pi/2, color='greenyellow', linestyle='--')
plt.axhline(y=np.pi/4, color='slateblue', linestyle='--')
plt.axhline(y=3*np.pi/4, color='slateblue', linestyle='--')
plt.axvline(x=33600, color='greenyellow', linestyle='--')
plt.axvline(x=29600, color='slateblue', linestyle='--')
plt.axvline(x=38000, color='slateblue', linestyle='--')
#plt.xlim(9,5500)
plt.yticks( [0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi],[ r'$0$', r'$\pi/4$', r'$\pi/2$', r'$3/4\pi$', r'$\pi$'])
plt.plot (a, d, 'rx', label='Messwerte')
#plt.plot(t, f(t, *params), 'b-' ,label='Ausgleichsfunktion f(x)')
plt.xlabel(r'$\nu\:/\:\mathrm{Hertz}$')
plt.ylabel(r'$ \phi \: / \:$ rad')
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig('plot5.pdf')
plt.show()
