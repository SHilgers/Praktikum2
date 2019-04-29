import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat

t, T1,T2,T3,T4,T5,T6,T7,T8 = np.genfromtxt('Run1org.txt', unpack=True)
t=t*5

ln= np.linspace(0, 2100)

plt.plot (t,T1, 'r-', label='Messingstab, breit, fern')
plt.plot (t,T4, 'b-', label='Messingstab, dünn, fern')


plt.xlabel(r't/ s')
plt.ylabel(r'T/ °C')

plt.legend()
plt.grid()
plt.savefig('T14.pdf')
