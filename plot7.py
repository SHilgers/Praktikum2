import numpy as np
from numpy import exp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.stats import sem

a = np.genfromtxt('Barium.txt', unpack=True)
b = np.linspace(1, 8191, 8192)
k= ufloat(0.403169, 0.000029)
c =b*k
b= b*0.403169-3.034

plt.plot (b[0:2000], a[0:2000], 'k-', label='Messwerte')
plt.grid()
plt.xlabel(r'$ E_{γ}\: /\: keV$')
plt.ylabel(r'Counts')
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('Ba.pdf')
plt.show()
