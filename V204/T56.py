import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat
from pylab import *
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

t, T1,T2,T3,T4,T5,T6,T7,T8 = np.genfromtxt('Run2org.txt', unpack=True)
t=t*2
ax=subplot(111)
ln= np.linspace(0, 2100)

plt.plot (t,T5, 'r-', label='Aluminiumstab, fern')
plt.plot (t,T6, 'b-', label='Aluminiumstab, nah')

ax.xaxis.set_major_locator(MultipleLocator(100))
ax.xaxis.set_major_formatter(FormatStrFormatter('%d'))
ax.xaxis.set_minor_locator(MultipleLocator(20))

ax.yaxis.set_major_locator(MultipleLocator(2))
ax.yaxis.set_minor_locator(MultipleLocator(1))

ax.xaxis.grid(True,'minor')
ax.yaxis.grid(True,'minor')
ax.xaxis.grid(True,'major',linewidth=1)
ax.yaxis.grid(True,'major',linewidth=1)

plt.xlabel(r't/ s')
plt.ylabel(r'T/ °C')
plt.legend()
plt.grid(b=True)
plt.show()
plt.savefig('T56.pdf')
