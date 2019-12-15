import numpy as np
from numpy import exp
import uncertainties.unumpy as unp
import math
import scipy.constants as sc
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.stats import sem

phi, Imax, Imin, Kb= np.genfromtxt('Werte1.txt', unpack=True)
phi=phi/360 *(2*np.pi)

K=(Imax-Imin)/(Imax+Imin)

print('Kontrast=', K)

x = np.linspace(0, 3.5 ,1000)
plt.plot (phi , K,'r+', label='Messdaten')
#plt.plot(phi, np.abs(np.sin(phi)*np.cos(phi)), 'g', label='Theoriekurve')

phi=phi[0:11]
K=K[0:11]
print('phi', phi)
def f(phi, a):
    return 2*a*(np.abs(np.sin(phi)*np.cos(phi)))
params, cov= curve_fit(f, phi, K)
errors = np.sqrt(np.diag(cov))
print('a =', params[0], '±', errors[0])
#print('b =', params[1], '±', errors[1])

plt.plot(x[0:450], f(x,*params)[0:450],'b-', label='Regression')

plt.grid()
plt.xlabel(r'$\Phi$ in rad')
plt.xticks([0, 0.5*np.pi, np.pi], ['0', r'$\frac{\pi}{2}$', r'$\pi$'])
plt.ylabel(r'K')
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('plot1.pdf')
plt.show()
