import numpy as np
from numpy import exp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.stats import sem
from math import e

a = np.genfromtxt('Unbekannt.txt', unpack=True)
bbb = np.linspace(1, 8191, 8192)
b=bbb*0.403169-3.034
pa=ufloat(-191, 64)
pc=ufloat(2474, 3467)
pd=ufloat(-1.47, 0.19)

def f(x, a, b, c, z):
    return a + b * np.exp(-((x-z)/c)**2)
y=[199, 237, 469, 608, 740, 883, 1519, 1658, 1913, 1957, 2007, 2326, 2787, 2874,
3080, 3426, 3502, 3749, 4126, 4297, 4388, 4590, 5481]
wp=[10.47, 2.18, 3.555, 7.268, 18.414, 35.60, 45.49, 1.530, 4.892, 1.064, 1.262, 3.10, 14.91, 1.635, 5.831, 3.968, 2.389,  2.128, 1.048, 2.844, 15.31, 2.025, 4.913]
dp=[0.2, 0.19, 0.19, 0.022, 0.036, 0.07, 0.19, 0.007, 0.016, 0.013, 0.006, 0.01, 0.03, 0.007, 0.014, 0.011, 0.008, 0.010, 0.009, 0.010, 0.05, 0.012, 0.023]
akt = ufloat(1599, 29)
wi = [13669, 2402, 5758, 391, 511, 1148, 326, 1051, 697, 896, 1027]
di = [78, 41, 42, 20, 23, 31, 23, 43, 40, 35, 46]
for m in range (0,23):
    params1, cov1 = curve_fit(f, b[y[m]-25:y[m]+25], a[y[m]-25:y[m]+25], p0=(70, 4000 , 1.2, y[m]*0.403169-3.034))
    covv1 = np.sqrt(np.diag(cov1))
    #print('a1 ist ',params1[0],'pm',covv1[0], 'und b1 ist ',params1[1],'pm',covv1[1], 'und c1 ist ',params1[2],'pm',covv1[2], 'und z1 ist ',params1[3],'pm',covv1[3])

    v = ufloat(params1[1],covv1[1])
    z = ufloat(params1[3],covv1[3])
    vv = v/(pc*(z-pa)**(pd))
    u = ufloat(params1[2],covv1[2])
    I = u*v*(np.pi)**(1/2)
    P=ufloat(0.01*wp[m], 0.01*dp[m])
    L = P*4378*0.01558*(pc*(z-pa)**(pd))
    #print(format(I, '8.3f'))
    #print(format(L, '8.3f'))



mc=ufloat(16266, 214)
mp=ufloat(3641, 58)
vh =mp/mc
print(vh)
