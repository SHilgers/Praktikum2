import numpy as np
from numpy import exp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.stats import sem

a = np.genfromtxt('Caesium.txt', unpack=True)
b = np.linspace(1, 8191, 8192)

plt.plot (b, a, 'k-', label='Messwerte')
plt.grid()
plt.xlabel(r'Kanalnummer')
plt.ylabel(r'Counts')
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('Cs.pdf')
plt.show()
