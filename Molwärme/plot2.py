import numpy as np
from numpy import exp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.stats import sem

T, Cv, Cverr = np.genfromtxt('Werte3.txt', unpack=True)

x = np.linspace(100,300,1000)
plt.plot (T, Cv,'r+', label='Theoriedaten')
#plt.errorbar(T, Cv, Cverr, label='Messwerte')
plt.grid()
plt.xlabel(r'T in K')
plt.ylabel(r'$C_V$ in J/(molK)')
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('plot2.pdf')
plt.show()
