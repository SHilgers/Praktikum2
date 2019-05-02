import numpy as np
from numpy import exp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.stats import sem
from math import e

a = np.genfromtxt('Barium.txt', unpack=True)
bbb = np.linspace(1, 8191, 8192)
b=bbb*0.403169-3.034

pa=ufloat(-191, 64)
pc=ufloat(2474, 3467)
pd=ufloat(-1.47, 0.19)

def f(x, a, b, c, z):
    return a + b * np.exp(-((x-z)/c)**2)
y=[208, 693, 759, 891, 960]
wp=[0.3331, 0.0713, 0.1831, 0.6205, 0.0894]
dp=[0.003, 0.0006, 0.0011, 0.0019, 0.0006]
akt = ufloat(1599, 29)
wi = [13669, 2402, 5758, 391, 511, 1148, 326, 1051, 697, 896, 1027]
di = [78, 41, 42, 20, 23, 31, 23, 43, 40, 35, 46]
for m in range (0,5):
    params1, cov1 = curve_fit(f, b[y[m]-25:y[m]+25], a[y[m]-25:y[m]+25], p0=(70, 4000 , 1.2, y[m]*0.403169-3.034))
    covv1 = np.sqrt(np.diag(cov1))
    #print('a1 ist ',params1[0],'pm',covv1[0], 'und b1 ist ',params1[1],'pm',covv1[1], 'und c1 ist ',params1[2],'pm',covv1[2], 'und z1 ist ',params1[3],'pm',covv1[3])
    v = ufloat(params1[1],covv1[1])
    z = ufloat(params1[3],covv1[3])
    vv = v/(pc*(z-pa)**(pd))
    u = ufloat(params1[2],covv1[2])
    I = u*v*(np.pi)**(1/2)
    P=ufloat(wp[m], dp[m])
    L = P*4378*0.01558*(pc*(z-pa)**(pd))
    print(format(I, '8.3f'))
    print(format(L, '8.3f'))
