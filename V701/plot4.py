import numpy as np
from numpy import exp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.stats import sem
import matplotlib.mlab as mlab
from scipy.misc import factorial
import math
from scipy.stats import poisson
#%matplotlib inline
#math.factorial(n)
x,N= np.genfromtxt('Werte3.txt', unpack=True)
#x=x*10
N=N/10

#Mittelwert
Nm=np.mean(N)
mu = Nm
print('Mittelwert N=', Nm)
#Fehler
Nf=sem(N)
print('Fehler N=', Nf)

#Varianz=Quadrat der Standardabweichung, also dem Fehler Stem
v=Nf**2
print('Varianz von N=', v)

#def g(x):
#    return 1000*((2*np.pi*v)**(-0.5))*np.exp(-(((x)-Nm)**2)/2*v)

#def poisson(k):
#    return (Nm**k/math.factorial(k)) * np.exp(-Nm)
#def poisson(k):
#   return (5**k/math.factorial(k)) * np.exp(-5)

#poisson.pmf(k) = exp(-mu) * mu**k / k!

t=np.linspace(960, 1100)
#Histogramm
n,bins,patches=plt.hist(N, bins=8, normed=True)
#Gauß1
#gauss=mlab.normpdf(bins, Nm , v)
#plt.plot(bins, gauss, 'r', label='Gaußverteilung')
#Gauß2
mu, sigma = Nm, v # mean and standard deviation
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
            np.exp( - (bins - mu)**2 / (2 * sigma**2) ), linewidth=2, color='r' , label='Gaußverteilung')
#poisson
mean, var, skew, kurt = poisson.stats(mu, moments='mvsk')
x = np.arange(poisson.ppf(0.01, mu), poisson.ppf(0.99, mu))
plt.plot(x, poisson.pmf(x, mu), 'g-', ms=8, label='Poissonverteilung')
plt.xlabel(r'$ Zählrate\; N$')
plt.ylabel(r'relative Häufigkeit')
plt.tight_layout()
plt.legend()
plt.savefig('plot4.pdf')
plt.show()
