import numpy as np
from numpy import exp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.stats import sem


a = np.genfromtxt('Caesium.txt', unpack=True)
b = np.linspace(1, 8191, 8192)
k= ufloat(0.403169, 0.000029)
c =b*k
b= b*0.403169


def f(x, a, b, c, z):
    return a + b * np.exp(-((x-z)/c)**2)

acs = np.genfromtxt('Caesium.txt', unpack=True)
bc = np.linspace(1, 8191, 8192)
bcs=bc*0.403169-3.034
params2, cov2 = curve_fit(f, bcs[1649-25:1649+25], acs[1649-25:1649+25], p0=(70, 4000 , 1.2, 1649*0.403169-3.034))
covv2 = np.sqrt(np.diag(cov2))
x=np.linspace(1640*0.403169-3.034,1656*0.403169-3.034, 50000)

plt.axhline(y=875, color='slateblue', linestyle='-', label='$y_{1/2} \: ≈\: 875 $')
plt.axvline(x=660.58, color='slateblue', linestyle='-' )
plt.axvline(x=662.60, color='slateblue', linestyle='-')
plt.axhline(y=175, color='red', linestyle='-', label='$y_{1/10} \:≈\: 175 $')
plt.axvline(x=663.32, color='red', linestyle='-')
plt.axvline(x=659.61 , color='red', linestyle='-')
plt.plot (bcs[1640:1656], a[1640:1656], 'kx', label='Messwerte')
#plt.plot (x, f(x, *params2), 'r-', label='Gaußverteilung')
plt.grid()
plt.xlabel(r'$ E_{γ}\: /\: keV$')
plt.ylabel(r'Counts')
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('plot6.pdf')
plt.show()
