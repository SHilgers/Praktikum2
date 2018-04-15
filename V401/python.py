import numpy as np
from numpy import exp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.stats import sem

a, b, c= np.genfromtxt('Werte2.txt', unpack=True)
f=a/5.017
#print(f)
a=a*10**(-3)
l=2*0.598*10**(-3)/c
print(l)
n = np.mean(l)
m =sem(l)
print('Mittelwert', n, 'Fehler', m)
