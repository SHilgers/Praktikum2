import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.stats import sem

x,y = np.genfromtxt('Werte4.txt', unpack=True)
x0=ufloat(24.89, 12)
phi=(x-x0)/1085
a=np.mean(phi)
print(a)
