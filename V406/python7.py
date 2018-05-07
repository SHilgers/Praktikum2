import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.stats import sem

x,y = np.genfromtxt('Werte2.txt', unpack=True)
x1=ufloat(3.76, 0.03)
x2=ufloat(0.05, 0.01)
x0=(x1-x2)/2
phi=(x-x0)/1085
a=np.mean(phi)
print(a)

i=ufloat(3.42, 0.27)
i=ufloat(3.7, 0.3)
print(np.mean(i))
