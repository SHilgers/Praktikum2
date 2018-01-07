import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.stats import sem

a = np.array([[336, 333, 337 ]])
#print(a.std())
#print(np.mean(a))

l= ufloat(10.11, 0.03)
c= ufloat(2.098, 0.006)
x = ufloat(509.5 , 0.5)
r= 2*((l*10**(-3))/(c*10**(-9)))**(1/2)
print(r)

q= (1/(x+50)) * ((l*10**(-3))/(c*10**(-9)))**(1/2)
print('q = ',q)

b= (x+50)/((l*10**(-3))*2*np.pi)
print('breite= ', b)
l=l*10**(-3)
c=c*10**(-9)
f=(((1/(l*c))-(((x+50)**2)/(2*l**2)))**(1/2))/(2*np.pi)
g= (((x+50)/(2*l))+(((x+50)**2)/(4*l**2)+1/(l*c))**(1/2))/(2*np.pi)
h= (-((x+50)/(2*l))+(((x+50)**2)/(4*l**2)+1/(l*c))**(1/2))/(2*np.pi)
print('res= ', f, 'v1= ', g, 'v2= ', h)
