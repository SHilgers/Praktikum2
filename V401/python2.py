import numpy as np
from numpy import exp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.stats import sem

a= np.genfromtxt('Werte1.txt', unpack=True)
l = ufloat(613.46 *10**(-9), 0.72 * 10**(-9))

n = 1 + a*l/(2*0.05)*(295.15/273.15)*(1.0132/(-0.2132+1.0132))
print(n)
q = np.mean(n)
#m =sem(n)
print('Mittelwert', q)#, 'Fehler', m)
n
o = 1 + a*613.46 *10**(-9)/(2*0.05)*(295.15/273.15)*(1.0132/(-0.2132+1.0132))
m =sem(o)
print('Mittelwertfehler =', m)
