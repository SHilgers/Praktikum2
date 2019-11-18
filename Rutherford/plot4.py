import numpy as np
from numpy import exp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.stats import sem

x1, y = np.genfromtxt('Werte3.txt', unpack=True)
def f(x, a,b):
    return a*x+b
dy=y**(0.5)
y1=y/360
dy1=dy/360

lam=ufloat(50.77*10**(-12),0.07*10**(-12))
A= np.e**(-50.77*10**(-12)*9131*24*60*60)*330000
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
Ak=y1
Akt=317000
xgrad=x1*(2*np.pi)/360
dAkt=dy1
WQ=Ak/(dx*O**2*A*N)
dWQ=dAkt/(dx*O**2*A*N)
print(WQ)
WQtheo=4*79**2*e**4/((4*np.pi*e0)**2*16*Ea**2*(np.sin(xgrad/2))**4)
print(WQtheo)


plt.errorbar(x1, WQ, xerr=0, yerr=dWQ  ,fmt='r.',label='Experimenteller Wirkungsquerschnitt')
#plt.plot (x1,WQ ,'bx', label='Experimenteller Wirkungsquerschnitt')
plt.plot (x1,WQtheo ,'bx', label='Theoretischer Wirkungsquerschnitt')
plt.xlabel(r'Winkel/°')
plt.ylim([10**(-25),10**(-18)])
plt.ylabel(r'WQ/m$^2$')
plt.yscale('log')
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('plot3.pdf')
plt.show()
