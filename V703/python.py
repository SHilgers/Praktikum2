import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.stats import sem


a, b, c, f, k= np.genfromtxt('Werte1.txt', unpack=True)
k=k*10**(-6)

d= np.sqrt(b)
g=b/60
h=np.sqrt(g)
#print(h,g)
e0=1.6022*10**(-19)


n1 = ufloat(12835/60, 113/60)
n2 = ufloat(15937/60, 126/60)
n12 = ufloat(28081/60, 168/60)

ta = 10**6*(n1+n2-n12)/(2*n1*n2)
#print(ta)
y, t = np.genfromtxt('Werte2.txt', unpack=True)
l = np.mean(t)
p =sem(t)
#print(l, 'pm ', p)
z=k*60/(b*e0)
fehler = k*60*c/(b*b*e0)

print(z, fehler)
