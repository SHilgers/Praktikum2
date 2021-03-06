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

m, T, I= np.genfromtxt('Dipol1.txt', unpack=True)
ma, Ta, Ia= np.genfromtxt('Dipol1Abzug.txt', unpack=True)

T=T+273.15 #Temperatur in K
Ta=Ta+273.15
t=np.arange(0, 50)

#Mittlere Heizrate bestimmen
diff=np.diff(T)

print('Mittelwert Heizrate diff=', np.mean(diff), sem(diff))
H=ufloat(np.mean(diff),sem(diff))
print('Heizrate=', H)

######Plot/Fit Untergrung########
x = np.linspace(220, 325)
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
plt.savefig('Dipol1mitUntergrund.png')
plt.show()

#Untergrund abziehen
Iohne=I-fit(T,*params)
#print('I ohe Untergrund=',Iohne)
plt.plot(T, Iohne,'r+', label='Messdaten ohne Untergrund')
plt.plot(T[9:26], Iohne[9:26],'b+', label='Messdaten für Integral')
plt.plot(T[9:19], Iohne[9:19],'k+', label='Messdaten für Anlaufkurve')
plt.grid()
plt.xlabel(r'$T$ in K')
plt.ylabel(r'$I$ in pA')
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('Dipol1ohneUntergrund.png')
plt.show()

#####Aktiviungsarbeit aus Anlaufkurve
u = np.linspace(0.00385, 0.00417)
TAnlauf=T[9:19]
IAnlauf=np.log(Iohne[9:19])
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
plt.ylabel(r'$ln(I)$')
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('Dipol1Anlauf.png')
plt.show()

W1=params2[0]*const.k/const.e #Berechnung der Aktivierungsenergie W=c*k und umrechnen in eV
print('Aktivierungsarbeit über Anlauf (eV)=', W1)


#####Polarisationsansatz/ Integral
Tint=T[9:26] #Für Integral verwendete Werte
Iint=Iohne[9:26] #Für Integral verwendete Werte
I_int = integrate.cumtrapz(Iint, Tint, initial=Iint[0]) #Integral berechnen
IInt=np.log(I_int/Iint)
print('Iint', Iint)
print('Tint', Tint)
print('I_int', I_int)
print('IInt=', IInt)

def Integral(Tint,Iint,H):
    array = np.array([])
    for b in Tint:
        array = np.append(array, np.trapz(Iint[Tint >= b], Tint[Tint >= b]))
    return array

Integ = Integral(Tint, Iint, H)
print('Iteg=', Integ)
Integ=Integ/Iint
Integ = Integ[Integ > 0] #negative Werte rausschmeißen
Integ = np.log(Integ)
print('Iteg=', Integ)

############ Ohne log
plt.plot(1/Tint, I_int/Iint ,'r+', label='Integral')
plt.grid()
plt.xlabel(r'$1/T$ in K')
plt.ylabel(r'$f(T)$ in pA')
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('Dipol1Int.png')
plt.show()
###############

#plt.plot(1/Tint, IInt ,'r+', label='Integral')
plt.plot(1/Tint[1:], Integ ,'r+', label='Integral')
t = np.linspace(0.00362, 0.00418)
def h(x ,e, f):
    return -e*x+f

params3, cov3= curve_fit(h, 1/Tint[1:],  Integ)
errors3 = np.sqrt(np.diag(cov3))
print('e =', params3[0], '±', errors3[0])
print('f =', params3[1], '±', errors3[1])

plt.plot(t, h(t,*params3),'b-', label='Regression')
plt.grid()
plt.xlabel(r'$1/T$ in K')
plt.ylabel(r'$lnf(T)$')
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('Dipol1Integral.png')
plt.show()

W2=params3[0]*const.k/const.e #Berechnung der Aktivierungsenergie W=c*k und umrechnen in eV
print('Aktivierungsarbeit über Integral (eV)=', W2)

####Relaxationszeit
Tmax=259.25 #K
taumax1=(const.k*Tmax**2)/(H*W1*const.e) #W wieder in J umrechnen
taumax2=(const.k*Tmax**2)/(H*W2*const.e)

print('Relaxationszeit taumax Anlauf=', taumax1)
print('Relaxationszeit taumax Integral=', taumax2)
#tau0 berechnen
tau01=taumax1/np.exp((W1*const.e)/(const.k*Tmax))
tau02=taumax2/np.exp((W2*const.e)/(const.k*Tmax))

print('Relaxationszeit tau0 Anlauf=', tau01)
print('Relaxationszeit tau0 Integral=', tau02)
