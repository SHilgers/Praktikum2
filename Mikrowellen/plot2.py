import numpy as np
from numpy import exp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.stats import sem

U4, A4= np.genfromtxt('Werte4.txt', unpack=True)
U5, A5= np.genfromtxt('Werte5.txt', unpack=True)
U6, A6= np.genfromtxt('Werte6.txt', unpack=True)

def f(x, a, b, c):
    return -a*(x-b)**2 +c
params, cov= curve_fit(f, U4, A4)
errors = np.sqrt(np.diag(cov))
print('m =', params[0], '±', errors[0])
print('b =', params[1], '±', errors[1])

params2, cov2= curve_fit(f, U5, A5)
errors = np.sqrt(np.diag(cov))
print('m =', params[0], '±', errors[0])
print('b =', params[1], '±', errors[1])

params3, cov3= curve_fit(f, U6, A6)
errors = np.sqrt(np.diag(cov))
print('m =', params[0], '±', errors[0])
print('b =', params[1], '±', errors[1])

x = np.linspace(0,300, 300)
plt.plot (U4 , A4,'bo', label='Messwerte')
plt.plot (U5 , A5,'bo')
plt.plot (U6 , A6,'bo')
#plt.plot (x, -(x-82)**2 +220  ,'r+')
#plt.plot(x[7:20], x[7:20])

plt.plot(x[68:92], f(x,*params)[68:92],'r-', label='Ausgleichsgerade')
plt.plot(x[119:150], f(x,*params2)[119:150],'r-')
plt.plot(x[201:233], f(x,*params3)[201:233],'r-')


plt.grid()
plt.xlabel(r'U in V')
plt.ylabel(r'$Amplitude $ in mV')
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('plot2.pdf')
plt.show()
