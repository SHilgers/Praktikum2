import numpy as np
from numpy import exp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.stats import sem

a, b, c, d= np.genfromtxt('Werte2.txt', unpack=True)

v =2*c/d *10**3
#print(v)
a, b= np.genfromtxt('Werte4.txt', unpack=True)

v2 =a/b *10**3
print(v2)

a, b= np.genfromtxt('Werte6.txt', unpack=True)

m1 = np.mean(a)
f1 = sem(a)
m2 = np.mean(b)
f2 = sem(b)
print(m1,f1,m2,f2)
