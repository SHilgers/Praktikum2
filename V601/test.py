import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat

a=7.29735*10**(-3)
R=2.179783*10**(-18)

Z, E= np.genfromtxt('test.txt', unpack=True)

s=Z-((4/a)*np.sqrt(E/R)-(5*E/R))**(1/2)*((1+(19/32)*a**2)*(E/R))**(1/2)

print(s)
