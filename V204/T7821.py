import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat


t, T1,T2,T3,T4,T5,T6,T7,T8 = np.genfromtxt('Run1org.txt', unpack=True)
t=t*5

a= T7-T8
b= T2-T1
ln= np.linspace(0, 400)

plt.plot (t,a, 'r-', label='$\Delta T_{78}=T7-T8$')
plt.plot (t,b, 'b-', label='$ \Delta T_{21}=T2-T1$')



plt.xlabel(r't/ s')
plt.ylabel(r'$\Delta T$/ °C')
plt.legend()
plt.grid()
plt.savefig('T7821.pdf')
