import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.stats import sem
a, b, c = np.genfromtxt('Werte7.txt', unpack=True)

d= a*c/b
print(d)

e = np.mean(d)
f =np.std(d, ddof=1) / np.sqrt(len(d))
g =sem(d)

j= e*np.sqrt(0.002*0.002+0.005*0.005)
print (e, f, g, 'Gaus=', j)
