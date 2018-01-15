import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat

t, T1,T2,T3,T4,T5,T6,T7,T8 = np.genfromtxt('Run1org.txt', unpack=True)
T=t*5

ln= np.linspace(0, 2100)

plt.plot (t,T5, 'r-', label='Aluminiumstab, fern')
plt.plot (t,T8, 'b-', label='Edelstahlstab, fern')


plt.xlabel(r't/ s')
plt.ylabel(r'T/ °C')
plt.legend()
plt.grid()
plt.savefig('T58.pdf')
