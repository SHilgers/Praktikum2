import numpy as np
from numpy import exp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.stats import sem

T, Cv, Cverr, Terr = np.genfromtxt('Werte3.txt', unpack=True)
x = np.linspace(100,300,1000)
#plt.plot (T, Cv,'r+', label='Messwerte')
plt.errorbar(T, Cv,xerr= Terr, yerr=Cverr, fmt='k.',  label='Messwerte')
#plt.errorbar(t, N, yerr=y_err, fmt='.')
#plt.errorbar(T + Terr, T + Cverr, xerr=0.4, yerr=Cverr, fmt='.')
plt.grid()
plt.xlabel(r'T in K')
plt.ylabel(r'$C_V$ in J/(molK)')
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('plot2.pdf')
plt.show()
