import numpy as np
from numpy import exp
from numpy import sqrt
import scipy.constants as const
import uncertainties.unumpy as unp
from uncertainties import ufloat
from uncertainties import ufloat_fromstr
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
from scipy.stats import sem
import math
import scipy.constants as sc
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from scipy import integrate

m, T, I= np.genfromtxt('Dipol2.txt', unpack=True)
ma, Ta, Ia= np.genfromtxt('Dipol2Abzug.txt', unpack=True)

T=T+273.15 #Temperatur in K
Ta=Ta+273.15
t=np.arange(0, 50)

#Mittlere Heizrate bestimmen
diff=np.diff(T)

print('Mittelwert Heizrate diff=', np.mean(diff), sem(diff))
H=ufloat(np.mean(diff),sem(diff))
print('Heizrate=', H)
######Plot/Fit Untergrung########
x = np.linspace(220, 330)
plt.plot (T, I,'r+', label='Messdaten')
plt.plot (Ta, Ia,'rx', label='Messdaten für Fit')

def fit(x ,a, b):
    return a*np.exp(-b/x)

params, cov= curve_fit(fit, Ta, Ia)
errors = np.sqrt(np.diag(cov))
print('a =', params[0], '±', errors[0])
print('b =', params[1], '±', errors[1])

plt.plot(x, fit(x,*params),'b-', label='Regression')
plt.grid()
plt.xlabel(r'$T$ in K')
plt.ylabel(r'$I$ in pA')
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('Dipol2mitUntergrund.png')
plt.show()

#Untergrund abziehen
Iohne=I-fit(T,*params)
#print('I ohne Untergrund=',Iohne)
plt.plot(T, Iohne,'r+', label='Messdaten ohne Untergrund')
plt.plot(T[10:42], Iohne[10:42],'b+', label='Messdaten für Integral')
plt.plot(T[10:28], Iohne[10:28],'k+', label='Messdaten für Anlaufkurve')
plt.grid()
plt.xlabel(r'$T$ in K')
plt.ylabel(r'$I$ in pA')
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('Dipol2ohneUntergrund.png')
plt.show()

#####Aktivierungsarbeit aus Anlaufkurve
u = np.linspace(0.00391, 0.00423)
TAnlauf=T[10:28]
IAnlauf=np.log(Iohne[10:28])
plt.plot(1/TAnlauf, IAnlauf,'r+', label='Messdaten')


def g(x ,c, d):
    return -c*x+d

params2, cov2= curve_fit(g, 1/TAnlauf,  IAnlauf)
errors2 = np.sqrt(np.diag(cov2))
print('c =', params2[0], '±', errors2[0])
print('d =', params2[1], '±', errors2[1])

plt.plot(u, g(u,*params2),'b-', label='Regression')
plt.grid()
plt.xlabel(r'$1/T$ in 1/K')
plt.ylabel(r'$ln(I)$ in ln(pA)')
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('Dipol2Anlauf.png')
plt.show()

W1=params2[0]*const.k/const.e #Berechnung der Aktivierungsenergie W=c*k und umrechnen in eV
print('Aktivierungsarbeit über Anlauf (eV)=', W1)


#####Polarisationsansatz/ Integral
Tint=T[10:42] #Für Integral verwendete Werte
Iint=Iohne[10:42] #Für Integral verwendete Werte
I_int = integrate.cumtrapz(Iint, Tint, initial=Iint[0]) #Integral berechnen
IInt=np.log(I_int/Iint)
#print('Iint', Iint)
#print('Tint', Tint)
#print('I_int', I_int)
#print('IInt=', IInt)


############ Ohne log
plt.plot(1/Tint, I_int/Iint ,'r+', label='Integral')
plt.grid()
plt.xlabel(r'$1/T$ in K')
plt.ylabel(r'$f(T)$ in pA')
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('Dipol2Int.png')
plt.show()
###############

plt.plot(1/Tint, IInt ,'r+', label='Integral')
t = np.linspace(0.0037, 0.00423)
def h(x ,e, f):
    return -e*x+f

params3, cov3= curve_fit(h, 1/Tint,  IInt)
errors3 = np.sqrt(np.diag(cov3))
print('e =', params3[0], '±', errors3[0])
print('f =', params3[1], '±', errors3[1])

plt.plot(t, h(t,*params3),'b-', label='Regression')
plt.grid()
plt.xlabel(r'$1/T$ in K')
plt.ylabel(r'$lnf(T)$ in pA')
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('Dipol2Integral.png')
plt.show()

W2=params3[0]*const.k/const.e #Berechnung der Aktivierungsenergie W=c*k und umrechnen in eV
print('Aktivierungsarbeit über Integral (eV)=', W2)


####Relaxationszeit
Tmax=255.05 #K
taumax1=(const.k*Tmax**2)/(H*W1)
taumax2=(const.k*Tmax**2)/(H*W2)

print('Relaxationszeit Anlauf=', taumax1)
print('Relaxationszeit Integral=', taumax2)
