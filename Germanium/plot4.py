import numpy as np
from numpy import exp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.stats import sem


def f(x, a, c, d):
    return c*(x-a)**(d)

wx=[244.6974, 344.2785, 411.1165, 443.965,
778.9045, 867.380, 964.079, 1085.837, 1112.076, 1408.013]
dx=[0.0008, 0.0012, 0.0012, 0.003, 0.0024,
0.003, 0.018, 0.010, 0.003, 0.003]
wq=[ 0.3549, 0.2416, 0.1949, 0.1827, 0.0987,
0.0857, 0.0809, 0.0768, 0.0745, 0.0550]
dq=[0.0090, 0.0048, 0.0106, 0.0089, 0.0032,
0.0063, 0.0036, 0.0046, 0.0032, 0.0027]

#for m in range (0,11):
#    x[m]=array(wx[m],dx[m])
#    y[m]=array(wy[m],dy[m])
params, cov = curve_fit(f, wx, wq, sigma=dq, p0=(-130, 700 ,-1.5), absolute_sigma=True)
errors = np.sqrt(np.diag(cov))
#print('a= ',params[0],' +- ', errors[0], b= ', params[1],' +- ', errors[1])
print('a =', params[0], '±', errors[0])
print('c =', params[1], '±', errors[1])
print('d =', params[2], '±', errors[2])
#print('d =', params[3], '±', errors[3])

x=np.linspace(2,1500, 50000)

plt.plot (x, f(x, *params), 'r-', label='$ Q(E_{γ})$')
plt.errorbar(wx, wq, xerr=dx, yerr=dq  ,fmt='k.',label='Messwerte')
#plt.plot (wx, wq, 'kx', label='Messwerte')
plt.xlabel(r'$ E_{γ}\: /\: keV$ ')
plt.ylabel(r'Q')
plt.ylim(0, 1)
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('plot4.pdf')
plt.show()
