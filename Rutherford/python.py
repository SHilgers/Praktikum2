import numpy as np
from numpy import exp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.stats import sem
import math
x1, y1 = np.genfromtxt('Werte3.txt', unpack=True)
def f(x, a,b):
    return a*x+b

dy1 = (y1)**(0.5)
#print(dy1)

#print(y1/360)
#print(dy1/360)

lam=ufloat(50.77*10**(-12),0.07*10**(-12))
A= np.e**(-lam*9131*24*60*60)*330
#print(A)

Ed=ufloat(1.37*10**6*1.602176*10**(-19),0.11*10**6*1.602176*10**(-19))
Ea=5.638*10**6*1.602176*10**(-19)
E=2*10**6*1.602176*10**(-19)
me= 9.109383*10**(-31)
ma=6.64*10**(-27)
v=(2*Ea/ma)**(0.5)
e0=8.854187*10**(-12)
N=5.895*10**28
Na=6.022*10**23
e=1.602*10**(-19)
c=299792500

x=Ed*me*v**2*(4*np.pi*e0)**2/(4*np.pi*e**4*N*4*79*(np.log(2*me*v**2/((9.225*1.602176*10**(-19))*(1-v**2/c**2)))-v**2/c**2))
x2=E*me*v**2*(4*np.pi*e0)**2/(4*np.pi*e**4*N*4*79*(np.log(2*me*v**2/((9.225*1.602176*10**(-19))))))
#print(x)
#print(x2)


O=7.8*10**(-4)
dx=2*10**(-6)
A=y1/360
dA=(y1)**(1/2)/360
Akt=317000
xgrad=x1*(2*np.pi)/360

WQ=A/(dx*O**2*Akt*N)
#print(WQ)
WQtheo=4*79**2*e**4/((4*np.pi*e0)**2*16*Ea**2*(np.sin(xgrad/2))**4)
#print(WQtheo)
Abw=100*(WQtheo-WQ)/WQtheo
print(WQ)

Agold=ufloat(292/360,(292)**(1/2)/360)
Abis=ufloat(479/360,(479)**(1/2)/360)
Aal=ufloat(124/360,(124)**(1/2)/360)
dxgold=2*10**(-6)
dxbis=1*10**(-6)
dxal=3*10**(-6)
grad=7*(2*np.pi)/360
Ngold=5.895*10**28
Nbis=2.824*10**28
Nal=6.027*10**28

WQgold=Agold/(dxgold*O**2*Akt*Ngold)
WQtgold=4*79**2*e**4/((4*np.pi*e0)**2*16*Ea**2*(np.sin(grad/2))**4)

WQbis=Abis/(dxbis*O**2*Akt*Nbis)
WQtbis=4*83**2*e**4/((4*np.pi*e0)**2*16*Ea**2*(np.sin(grad/2))**4)

WQal=Aal/(dxal*O**2*Akt*Nal)
WQtal=4*13**2*e**4/((4*np.pi*e0)**2*16*Ea**2*(np.sin(grad/2))**4)

#print(WQgold,WQtgold,WQbis,WQtbis,WQal,WQtal)
