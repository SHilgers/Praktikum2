import numpy as np
from numpy import exp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.stats import sem

n, so, su, schieb= np.genfromtxt('Werte3.txt', unpack=True)
so=so-1.53
su=su-1.53
h=80
S=h-so-su
print(S)
f=(schieb-S)/(schieb)*100
print(f)



#s=np.mean(s)
#sf=np.sem(s)
#print('Tiefe s Mittel=', s, 'Fehler=', sf)

#bmf=ufloat(20.8 , 0.73)
