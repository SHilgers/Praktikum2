import numpy as np
from numpy import exp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.stats import sem
from math import e
import scipy.integrate as integrate

a = ufloat(1600, 20)
d1= ufloat(81, 2)
d2= ufloat(102, 2)
d3= ufloat(163, 2)
d4= ufloat(205, 2)

b1 = 1/80
b2 = 1/100

l1=(b1*d1)/(1*(a**2+d1**2)**(1/2))
l2=(b2*d2)/(1*(a**2+d2**2)**(1/2))
l3=(b1*d3)/(2*(a**2+d3**2)**(1/2))
l4=(b2*d4)/(2*(a**2+d4**2)**(1/2))

#print(l1,l2,l3,l4)
w=(632, 636, 633, 635)


m = np.mean(w)
n = sem(w)
print(m,n)

sum=(1/4)*(17**2+15**2+11**2+10**2)**(1/2)
print(sum)
