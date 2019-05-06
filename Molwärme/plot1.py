import numpy as np
from numpy import exp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.stats import sem

T, a = np.genfromtxt('alpha.txt', unpack=True)

def f(x, m, b):
    return m*1/x+b
params, cov= curve_fit(f, T, a)
errors = np.sqrt(np.diag(cov))

print('m =', params[0], '±', errors[0])
print('b =', params[1], '±', errors[1])


x = np.linspace(70,300,1000)
plt.plot (1/T, a,'r+', label='Theoriedaten')
plt.plot(1/x, f(x,*params),'b-', label='Ausgleichsgerade')
plt.grid()
plt.xlabel(r'1/T in 1/K')
plt.ylabel(r'$\alpha\cdot 10^{-6}$ in 1/K')
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('alpha.pdf')
plt.show()
