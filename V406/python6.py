import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.stats import sem

x,y = np.genfromtxt('Werte1.txt', unpack=True)
x0 =ufloat(0.13,1)

phi=(x-x0)/1085
a=np.mean(phi)
print(a)

i=ufloat(7.1, 2)
i=ufloat(8.1, 2)
print(np.mean(i))
