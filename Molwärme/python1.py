import numpy as np
from numpy import exp
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.stats import sem

Rp, Up, Ip, Rz, Uz, Iz, t, dt= np.genfromtxt('Werte.txt', unpack=True)
theta_t =  np.genfromtxt('Werte4.txt', unpack=True)
#Masse Kupferprobe
m=0.342
#molare Masse Kupfer in kg/mol
M=63.55*1e-3

def Temperatur(R):
 return 0.00134*R**2+2.296*R-243.02
#Fehler auf alle Werte
Rp=unp.uarray(Rp, 0.1)
Up=unp.uarray(Up, 0.1)
Ip=unp.uarray(Ip*1e-3, 0.1*1e-3)
Rz=unp.uarray(Rz, 0.1)
dt=unp.uarray(dt, 3)

print(Rp)
print(Up)
print(Ip)
print(dt)
#Temperaturen berechnen in °C
Tp=Temperatur(Rp)
Tz=Temperatur(Rz)
#Umrechnen in K
Tp=Tp+273.15
Tz=Tz+273.15
#Temperaturdifferenzen
dTp=np.diff(Tp)
dTz=np.diff(Tz)
#Cp berechnen
Cp=(Up[1:37]*Ip[1:37]*dt[1:37]*M)/(dTp*m)
print('Tp=',Tp)
print(".......................................................")
print('Tz=',Tz)
print(".......................................................")
print('dTp=',dTp)
print(".......................................................")
print('Cp=', Cp)
#Fit alpha
#m = -872.1995325995504 ± 3.788508415882174
#b = 19.40432105608779 ± 0.026873634041107146

m=ufloat(-0.000872, 0.00000379)
b=ufloat(0.00001940, 0.00000003)

def alpha(x):
    return m*1/x+b
#berechne alpha Werte
a=alpha(Tp[1:37])
k=137.8*10**9 #140GPa
V0=7.11*10**(-6) #m^3/mol
#berechne Cv
Cv=Cp-(9*a**2*k*V0*Tp[1:37])

print('a=', a)
print("......................................................")
print('Cv=', Cv)
print("......................................................")

#Debye Temperatur berechnen
theta= theta_t*Tp[1:20]
print('theta=', theta)
print('Mittelwert theta=', np.mean(theta[0:17]))
