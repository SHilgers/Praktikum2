import numpy as np
from numpy import exp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.stats import sem

x=(13,79,83)
y=(9.9*10**(-24),35.7*10**(-24),244*10**(-24))
dy=(0.9*10**(-24),2.1*10**(-24),11*10**(-24))
t=(0.2*10**(-24),7.3*10**(-24),8*10**(-24))

ly=np.log(y)
lx=np.log(x)

aw=(np.log(244*10**(-24))-np.log(9.9*10**(-24)))/(np.log(83)-np.log(13))
print(aw)
def f(x, a,b):
    return a*x+b

def g(x, a,b):
    return x**a*np.e**b
params, cov = curve_fit(f, lx, ly)
covv = np.sqrt(np.diag(cov))
print('a1 ist ',params[0],'pm',covv[0])
print('b1 ist ',params[1],'pm',covv[1])

l=np.linspace(13, 83, 50000)

plt.errorbar(x, y, xerr=0, yerr=dy  ,fmt='r.',label='Experimenteller Wirkungsquerschnitt')
#plt.plot (x1,WQ ,'bx', label='Experimenteller Wirkungsquerschnitt')
plt.plot (x,t ,'bx', label='Theoretischer Wirkungsquerschnitt')
plt.plot (l, g(l, *params), 'r-', label='Lineare Ausgleichsgerade')
#plt.plot (l, g(l, aw, -57.4033), 'g-', label='Lineare Ausgleichsgerade ohne Gold')
plt.xlabel(r'Z')
#plt.ylim([10**(-25),10**(-20)])
plt.ylabel(r'WQ/m$^2$')
plt.yscale('log')
plt.xscale('log')
plt.legend(loc="best")
plt.xticks([5,10,100])
#ax.set_xticks([1,5,10,50])
plt.tight_layout()
plt.savefig('plot5.pdf')
plt.show()
