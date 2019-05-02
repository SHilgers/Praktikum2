import numpy as np
from numpy import exp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.stats import sem
from math import e

a = np.genfromtxt('Europium.txt', unpack=True)
b = np.linspace(1, 8191, 8192)

def f(x, a, b, c, z):
    return a + b * np.exp(-((x-z)/c)**2)
y=[310, 614, 862, 1027, 1109, 1940, 2158, 2400, 2703, 2767, 3501]
wp=[28.41, 7.55, 26.59, 2.238, 3.120, 12.97, 4.243, 14.50, 10.13, 13.41, 20.85]
dp=[0.13, 0.04, 0.12, 0.010, 0.010, 0.06, 0.023, 0.06, 0.06, 0.06, 0.003]
akt = ufloat(1599, 29)
wi = [13669, 2402, 5758, 391, 511, 1148, 326, 1051, 697, 896, 1027]
di = [78, 41, 42, 20, 23, 31, 23, 43, 40, 35, 46]
for m in range (0,11):
    params1, cov1 = curve_fit(f, b[y[m]-25:y[m]+25], a[y[m]-25:y[m]+25], p0=(70, 4000 , 1.2, y[m]))
    covv1 = np.sqrt(np.diag(cov1))
    #print('a1 ist ',params1[0],'pm',covv1[0], 'und b1 ist ',params1[1],'pm',covv1[1], 'und c1 ist ',params1[2],'pm',covv1[2], 'und z1 ist ',params1[3],'pm',covv1[3])
    v = ufloat(params1[1],covv1[1])
    u = ufloat(params1[2],covv1[2])
    I = u*v*(np.pi)**(1/2)
    #print(I)
    p=ufloat(0.01*wp[m], 0.01*dp[m])
    I = p*akt*3598*0.01558
    #print(format(I, '8.0f'))
    iex = ufloat(wi[m], di[m])
    q=iex/I
    #print(format(q, '8.4f'))

#Ak = ufloat(4130,60)
#la = ufloat(1.6244*10**(-9),0.0019*10**(-9))
#print(e)
#Akt = Ak*e**(-la*584323200)
#print(Akt)
acs = np.genfromtxt('Caesium.txt', unpack=True)
bc = np.linspace(1, 8191, 8192)
bcs=bc*0.403169-3.034
params2, cov2 = curve_fit(f, bcs[1649-25:1649+25], acs[1649-25:1649+25], p0=(70, 4000 , 1.2, 1649*0.403169-3.034))
covv2 = np.sqrt(np.diag(cov2))
#print('a1 ist ',params2[0],'pm',covv2[0], 'und b1 ist ',params2[1],'pm',covv2[1], 'und c1 ist ',params2[2],'pm',covv2[2], 'und z1 ist ',params2[3],'pm',covv2[3])




k= ufloat(0.403169, 0.000029)
zcs= ufloat(1648.52076848, 0.02433831731)
Ecs = k*zcs
#print(format(Ecs, '8.3f'))
hb=ufloat(1.227,0.015)
hwb=hb*2*np.log(2)
#print(hwb)
zwb=hb*2*np.log(10)
#print(format(zwb, '8.3f'))
hc=ufloat(1674 ,17)
Ics=hc*hb*np.pi**(1/2)
print(format(Ics, '8.3f'))

params3, cov3 = curve_fit(f, bcs[495-25:495+25], acs[495-25:495+25], p0=(70, 4000 , 1.2, 495*0.403169-3.034))
covv3 = np.sqrt(np.diag(cov3))
print('a1 ist ',params3[0],'pm',covv3[0], 'und b1 ist ',params3[1],'pm',covv3[1], 'und c1 ist ',params3[2],'pm',covv3[2], 'und z1 ist ',params3[3],'pm',covv3[3])
