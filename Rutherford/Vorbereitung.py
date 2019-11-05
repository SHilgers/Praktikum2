import numpy as np
from numpy import exp
import uncertainties.unumpy as unp
import math
import scipy.constants as sc
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.stats import sem

Z=7.06
A=14.02
I=14.05 #16.04
u=1.66052873*10**(-27)
rho=1.29
e=1.602176*10**(-19)
E=5.48*10**(6)*e
ma=6.64*10**(-27)
m=9.109381*10**(-31)
z=2
ep=8.8541878*10**(-12)
R=8.314
T=300
M=0.8*14*u+0.2*16*u

v=np.sqrt((2*E/ma))
N=(rho/(A*u))

#-dE=(4*math.pi*(e**4)*(z**2)*N*Z)/(m*(v**2)*(4*math.pi*ep)**2) *(math.log(2*m*(v**2)/I))

ab=(4*math.pi*(e**4)*(z**2)*N*Z)/(m*(v**2)*(4*(math.pi)*ep)**2)
cd=math.log(2*m*(v**2)/I)
dE=ab*cd
dEE=dE/e


p=((1000*e/0.1)*m*(v**2)*R*T*rho*(4*math.pi*ep)**2)/(4*math.pi*(e**2)*(z**2)*M*Z*math.log((2*m*(v**2))/I))

print('N=', N)
print('v=', v)
print('ab=', ab)
print('cd=', cd)
print('E=', -dE)
print('dEE=', dEE)
print('p=', p)
