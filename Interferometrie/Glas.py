import numpy as np
from numpy import exp
from numpy import sqrt
import uncertainties.unumpy as unp
import math
import scipy.constants as sc
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat
from uncertainties import ufloat_fromstr
from scipy.stats import sem

M= np.genfromtxt('Werte2.txt', unpack=True)
mbar, M1, M2, M3= np.genfromtxt('Werte3.txt', unpack=True)

#Berechnung Glas
T=0.001 #in m
l=632.99*10**(-9) #in m
theta=12/360 *(2*math.pi)
t0=10/360 *(2*math.pi)

na=(2*theta*t0*T)/(2*theta*t0*T-M*l)

print('na=', na)
print('Mittelwert:', np.mean(na))
print('Abweichung:', sem(na))
#Berechnung Gas
L=ufloat(0.100,0.00001) #Länge in m

n1=(41*l/L)+1
n3=(40*l/L)+1
n2=(40*l/L)+1

print('n1=', n1)
print('Mittelwert:', np.mean(n1))
print('n2=', n2)
print('Mittelwert:', np.mean(n2))
print('n3=', n3)
print('Mittelwert:', np.mean(n3))
nn=[n1, n2, n3]
print(np.mean(nn))

mbar=mbar #Druck in Pa
Na=6.022*10**(23)
a=ufloat_fromstr("2.118(91)e-29")
#a=2.118*10**(-29)
R=8.3145
K=21.2+273.15 #Temperatur in K

nt=unp.sqrt(1+(4*math.pi*mbar*Na*a)/(R*K))

print('n durch Lorentz Lorenz=', nt)
print('Mittelwert=', np.mean(nt))
