import numpy as np
from numpy import exp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat

a, b= np.genfromtxt('Werte1.txt', unpack=True)
c, d= np.genfromtxt('Werte2.txt', unpack=True)
#a = a / 10**6 # in sec
#c=c*(1)/10**6 # in sec
a=a*10**(-6)
c=c*10**(-6)
def f(x, g, h):
    return g* (np.exp(-h*2*np.pi*x))


params, cov = curve_fit(f, a, b, p0=(50,500))

errors = np.sqrt(np.diag(cov))
#print('a= ',params[0],' +- ', errors[0], b= ', params[1],' +- ', errors[1])
print('g =', params[0], '±', errors[0])
print('h =', params[1], '±', errors[1])

parrams, covv = curve_fit(f, c, d, p0=(50,500))
errrors = np.sqrt(np.diag(covv))
#print('a= ',params[0],' +- ', errors[0], b= ', params[1],' +- ', errors[1])
print('g2 =', parrams[0], '±', errrors[0])
print('h2 =', parrams[1], '±', errrors[1])
p1= ufloat(params[1],errors[1])
p2=ufloat(parrams[1],errrors[1])
p3=(p1+p2)/2
print ('gesamt = ', p3)
l=ufloat(10.11*10**(-3), 0.03*10**(-3))
r= p3*4*np.pi*l
t=1/(2*np.pi*p3)
print ('r= ', r)
print('t= ', t)
#plt.plot(t, f(t, *params), 'b-' ,label='Lineare Regression')


x=np.linspace(0.000002, 0.000500, 10000)
#plt.xscale('log')
plt.xlim(0.000002, 0.0006)
plt.plot (a, b, 'rx', label='Messwerte Minima')
plt.plot (c, d, 'bx', label='Messwerte maxima')
plt.plot(x,f(x, *params), 'r-' ,label='Ausgleichsfunktion der Minima')
plt.plot(x,f(x, *parrams), 'b-' ,label='Ausgleichsfunktion der Maxima')
plt.grid()
plt.xlabel(r'$t \: /\: s$')
plt.ylabel(r'$ U \: / \: V$')
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('plot1.pdf')
plt.show()
