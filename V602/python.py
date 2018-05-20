import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat

h = 6.626070040*10**(-34)
c= 299792458
e0= 1.602176462*10**(-19)

lmin = 2*201.4*10**(-12)*np.sin(10/360*np.pi)
lmintheo = h*c/(e0*35000)
Emax = h*c/(lmin)
Emaxtheo = h*c/(lmintheo)
rell = (lmintheo-lmin)/lmintheo
relE = (Emaxtheo-Emax)/Emaxtheo
l1 = 2*201.4*10**(-12)*np.sin(40/360*np.pi)
l2 = 2*201.4*10**(-12)*np.sin(44.4/360*np.pi)
E1 = h*c/(l1*e0)
E2 = h*c/(l2*e0)
dE= E2-E1

print('Lmim = ', lmin,'Lmimtheo = ', lmintheo,'Emax = ', Emax, 'Emaxtheo = ', Emaxtheo,
    'rell = ', rell,'relE = ', relE,'dE = ', dE)
