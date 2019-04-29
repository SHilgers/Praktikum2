import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.stats import sem

x,y = np.genfromtxt('Werte3.txt', unpack=True)
x0=ufloat(26, 1)
phi=(x-x0)/1085
a=np.mean(phi)
print(a)

i=ufloat(5, 1)
i=ufloat(5.5 ,2)
print(np.mean(i))
