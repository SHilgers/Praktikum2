import numpy as np
from numpy import exp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat

T= np.genfromtxt('Werte1.txt', unpack=True)

p=5.5*10**(7)*np.exp((-6876)/T)
w=(0.0029)/p

print(p)
print(w)
