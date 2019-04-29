import numpy as np
from numpy import exp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat
t, a, b, c, d, p= np.genfromtxt('Werte.txt', unpack=True)

d=d+273.15
print(d)
