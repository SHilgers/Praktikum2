import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat


h = 6.626070040*10**(-34)
c= 299792458
e0= 1.602176462*10**(-19)

lbrom = 2*201.4*10**(-12)*np.sin(26.05/360*np.pi)
Ebrom = h*c/(lbrom*e0)
rbrom = (Ebrom-13500)/13500

lstr = 2*201.4*10**(-12)*np.sin(21.70/360*np.pi)
Estr = h*c/(lstr*e0)
rstr = (Estr-16100)/16100

lzink = 2*201.4*10**(-12)*np.sin(36.75/360*np.pi)
Ezink = h*c/(lzink*e0)
rzink = (Ezink-16100)/16100

lzir = 2*201.4*10**(-12)*np.sin(19.35/360*np.pi)
Ezir = h*c/(lzir*e0)
rzir = (Ezir-16100)/16100

print('lbrom =', lbrom, 'Ebrom =', Ebrom,'rbrom =', rbrom,
'lstr =', lstr, 'Estr =', Estr,'rstr =', rstr,
'lzink =', lzink, 'Ezink =', Ezink,'rzink =', rzink,
'lzir =', lzir, 'Ezir =', Ezir,'rzir =', rzir)
