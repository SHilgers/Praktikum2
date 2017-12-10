import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.stats import sem
a, b, c, d = np.genfromtxt('Werte5.txt', unpack=True)

j= b* c/d
k =a* d/c
print('R=', j, 'C= ', k)

l = np.mean(j)
m =sem(j)
n= l*np.sqrt(0.005*0.005+0.03*0.03)
print('Rm=', l, 'Rf= ', m, 'Rgaus=', n)

o = np.mean(k)
p =sem(k)
q= l*np.sqrt(0.005*0.005+0.002*0.002)
print('Cm=', o, 'Cf= ', p, 'Cgaus=', q)
