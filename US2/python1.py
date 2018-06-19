import numpy as np
from numpy import exp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.stats import sem

n, so, su, schieb= np.genfromtxt('Werte1.txt', unpack=True)
so=so-1.53
su=su-1.53
h=80
S=h-so-su
print(S)
f=(schieb-S)/(schieb)*100
print(f)


n, so2, su2= np.genfromtxt('Werte2.txt', unpack=True)
so2=so2-3
su2=su2-3
h=80
S2=h-so2-su2

print(S2)
