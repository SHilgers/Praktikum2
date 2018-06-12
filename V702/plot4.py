import numpy as np
from numpy import exp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat

x, y= np.genfromtxt('Werte1.txt', unpack=True)
Nu=215 #215 auf 900s
Nun=(215/900)*10
x=x*10
#y=np.log(y-Nun)
y=y-Nun

t=np.linspace(-1, 440)

plt.plot (x, y, 'rx', label='Messwerte')
#plt.plot(x,y, 'rx' )

plt.plot(x, 2.5*np.exp(-0.01122*x+ np.exp(1.45)))
#plt.plot(x, 90*np.exp(-0.0097*x), 'b-')
#plt.plot(x, 1*np.exp(-0.0015*x)+10, 'g--')
#plt.plot(x, (-11.22e-3)*x+ 4.73)
plt.xlabel(r'$ t/s$')
plt.ylabel(r'$ N$')
#plt.yscale('log')
plt.tight_layout()
plt.legend()
plt.savefig('plot4.pdf')
plt.show()
#(N=\SI{11,22(82)e-3}{\per\s}\cdot t+\SI{4,73(11)}\\
#(N=\SI{1,50(137)e-3}{\per\s}\cdot t +\SI{2,68(47)}\\
#(N=\SI{9,7(16)e-3}{\per\s}\cdot + \SI{2,0(5)}\\
