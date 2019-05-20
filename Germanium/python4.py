import numpy as np
from numpy import exp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.stats import sem
from math import e

E = [160.6121, 223.2368, 276.3989, 302.8508, 356.0129, 383.8485]
dE = [0.0016, 0.0013, 0.0012, 0.0005, 0.0007, 0.0012]

P= [0.00638, 0.00450, 0.0713, 0.1831, 0.6205, 0.0894]
dP= [0.00006, 0.00005, 0.0006, 0.0011, 0.0019, 0.0006]

C=[1.8 , 2.7, 1.922, 2.018, 2.112, 2.31]
dC=[0.6, 0.7, 0.024, 0.009, 0.006, 0.004]

B=[19, 22, 466, 1012, 2748, 343]
dB=[0.7, 5, 5, 4, 7, 4]

pc = ufloat(49,26)
pa = ufloat(60,30)
pd = ufloat(-0.93, 0.07)

for m in range (0,6):
    Em = ufloat(E[m], dE[m])
    Q = pc*(Em-pa)**(pd)
    #print(Q)
    cm = ufloat(C[m], dC[m])
    bm = ufloat(B[m], dB[m])
    I = cm*bm*(np.pi)**(1/2)
    #print(I)
    pm = ufloat(P[m], dP[m])
    l = pm*0.01558*4378*Q
    print(l)
