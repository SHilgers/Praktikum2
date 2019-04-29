import numpy as np
from numpy import log, pi
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.stats import sem
N=1
U1=4.3
I1=2
U2=4.7
I2=2.1
U3=5.1
I3=2.2
U4=5.4
I4=2.3
U5=5.9
I5=2.4
S1=0.1*10**(-3)
S2=0.23*10**(-3)
S3=0.55*10**(-3)
S4=1.07*10**(-3)
k=1.3806*10**(-23)
m=9.109*10**(-31)
h=6.626*10**(-34)
o=1.602*10**(-19)
r=0.32*10**(-4)
a=((U1*I1-N)/(0.32*0.28*5.7*10**(-12)))**(1/4)
b=((U2*I2-N)/(0.32*0.28*5.7*10**(-12)))**(1/4)
c=((U3*I3-N)/(0.32*0.28*5.7*10**(-12)))**(1/4)
d=((U4*I4-N)/(0.32*0.28*5.7*10**(-12)))**(1/4)
f=((U5*I5-N)/(0.32*0.28*5.7*10**(-12)))**(1/4)
print('T1= ',a ,'T2= ', b,'T3= ', c,'T4= ', d,'T5= ', f)
p1=(-k*a/o)*np.log(S1*h**3/(4*np.pi*o*r*m*k*k*a**2))
p2=(-k*b/o)*np.log(S2*h**3/(4*np.pi*o*r*m*k*k*b**2))
p3=(-k*c/o)*np.log(S3*h**3/(4*np.pi*o*r*m*k*k*c**2))
p4=(-k*d/o)*np.log(S4*h**3/(4*np.pi*o*r*m*k*k*d**2))
print('P1= ',p1,'P2= ', p2,'P3= ', p3,'P4= ', p4)

y=[4.74,4.80,4.82,4.85]
s =sem(y)
print('Fehler = ', s)
