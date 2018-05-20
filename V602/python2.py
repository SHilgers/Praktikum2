import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat

#24.3 29.65


h = 6.626070040*10**(-34)
c= 299792458

e0= 1.602176462*10**(-19)
R= 2.179783*10**(-18)
a= 7.29735*10**(-3)
Z= 29


l1 = 2*201.4*10**(-12)*np.sin(24.3/360*np.pi)
l2 = 2*201.4*10**(-12)*np.sin(29.65/360*np.pi)
E1 = h*c/(l1)
E2 = h*c/(l2)

dE = E2-E1
S1= Z-(((4/a)*(dE/R)**(1/2))-5*dE/R)**(1/2)
S2= (1+(19/32)*(a**2)*dE/R)**(1/2)
S=S1*S2
#print('S =', S)
print(dE)
