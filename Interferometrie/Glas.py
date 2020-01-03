import numpy as np
from numpy import exp
from numpy import sqrt
import uncertainties.unumpy as unp
from uncertainties import ufloat
from uncertainties import ufloat_fromstr
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
from scipy.stats import sem
import math
import scipy.constants as sc
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


MGl= np.genfromtxt('Werte2.txt', unpack=True)
mbar, M1, M2, M3, M, nr= np.genfromtxt('Werte3.txt', unpack=True)

#Berechnung Glas
T=0.001 #in m
l=632.99*10**(-9) #in m
theta=11/360 *(2*math.pi)
t0=10/360 *(2*math.pi)

na=(2*theta*t0*T)/(2*theta*t0*T-MGl*l)

print('na=', na)
print('Mittelwert:', np.mean(na))
print('Abweichung:', sem(na))

#Berechnung Gas
L=ufloat(0.100,0.00001) #Länge in m

n1=(41*l/L)+1
n2=(40*l/L)+1
n3=(40*l/L)+1

print('n1=', n1)
print('Mittelwert:', np.mean(n1))
print('n2=', n2)
print('Mittelwert:', np.mean(n2))
print('n3=', n3)
print('Mittelwert:', np.mean(n3))
nn=[n1, n2, n3]
print(np.mean(nn))


p=100*mbar #Druck in Pa
Na=6.022*10**(23)
a=ufloat_fromstr("2.118(91)e-29") #Konstante nicht mehr verwendet
#a=2.118*10**(-29)
R=8.3145
K=21.2+273.15 #Temperatur in K

n=(M*l/L)+1

print('n in Abh. von p=', n)
#nt=unp.sqrt(1+(4*math.pi*p*Na*a)/(R*K))

#print('n durch Lorentz Lorenz=', nt)
#print('Mittelwert=', np.me0an(nt))

x = np.linspace(0, 1000 ,1000)
plt.plot (mbar , nr,'r+', label='Messdaten')


def f(x, b):
    return (1+(b*x)/(R*K))**(1/2)

params, cov= curve_fit(f, mbar, nr)
errors = np.sqrt(np.diag(cov))
print('a =', params[0], '±', errors[0])

B=ufloat(params[0], errors[0])

plt.plot(x, f(x,*params),'b-', label='Regression')

plt.grid()
plt.xlabel(r'$p$ in mbar')
plt.ylabel(r'n')
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('Glasplot.pdf')
plt.show()

#Berechnung bei Normatmosphäre
pnor= 1013.25 #Normaldruck
Tnor=15+273.15
n=(1+(B*pnor)/(R*Tnor))**(1/2)
#n=(1+(B*950)/(R*294.35))**(1/2)
print('n bei Normdruck=', n)
