import numpy as np
from numpy import exp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat

x1, x2, x3, y1= np.genfromtxt('Werte1.txt', unpack=True)
x4, y2 = np.genfromtxt('Werte11.txt', unpack=True)
x5,y3 = np.genfromtxt('Werte12.txt', unpack=True)
y1=y1*0.625
y2=y2*0.625
y3=y3*0.625

def f(x, a, b):
    return a*x+b

params1, cov1 = curve_fit(f, x1, y1)
params2, cov2 = curve_fit(f, x2, y1)
params3, cov3 = curve_fit(f, x3, y1)
params4, cov4 = curve_fit(f, x4, y2)
params5, cov5 = curve_fit(f, x5, y3)

errors1 = np.sqrt(np.diag(cov1))
errors2 = np.sqrt(np.diag(cov2))
errors3 = np.sqrt(np.diag(cov3))
errors4 = np.sqrt(np.diag(cov4))
errors5 = np.sqrt(np.diag(cov5))

print('a1 =', params1[0], '±', errors1[0])
print('a2 =', params2[0], '±', errors2[0])
print('a3 =', params3[0], '±', errors3[0])
print('a4 =', params4[0], '±', errors4[0])
print('a5 =', params5[0], '±', errors5[0])

#print(x)
t=np.linspace(-25, 35)
plt.plot (x1, y1, 'rx', label='U=180')
plt.plot (x2, y1, 'bx', label='U=220')
plt.plot (x3, y1, 'gx', label='U=270')
plt.plot (x4, y2, 'mx', label='U=370')
plt.plot (x5, y3, 'yx', label='U=500')
plt.plot(t,f(t, *params1), 'r-' ,label='Ausgleichsgerade')
plt.plot(t,f(t, *params2), 'b-' ,label='Ausgleichsgerade')
plt.plot(t,f(t, *params3), 'g-' ,label='Ausgleichsgerade')
plt.plot(t,f(t, *params4), 'm-' ,label='Ausgleichsgerade')
plt.plot(t,f(t, *params5), 'y-' ,label='Ausgleichsgerade')
plt.xlabel(r'$ U_d /\: \mathrm{V}$')
plt.ylabel(r'$ D /\: \mathrm{cm} $')
plt.tight_layout()
plt.legend()
plt.savefig('plot1.pdf')
plt.show()
