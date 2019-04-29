import numpy as np
from numpy import exp, sin
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.stats import sem

a, b= np.genfromtxt('Werte1.txt', unpack=True)

c = (1/2)*(b-a)
#print(c)
m1 = np.mean(c)
f1 = sem(c)
#print (m1, 'pm ', f1)
l, m, n = np.genfromtxt('Werte2.txt', unpack=True)
m2 = m+180
o = (n-m2)
#print(o)
m1= m1*np.pi/180
f3=f1*np.pi/180
o = o*np.pi/180
y = ufloat(m1, f1)
w1= np.sin((o+m1)/2)
w2= np.sin(m1/2)
w=w1/w2
#print(w)

v1=np.sin(o/2)
v2=np.sin(m1/2)
v=((v1/v2)**2*f1**2)**(1/2)
#print(v)

yer= v**2
yw= w**2
print(yw)
p1= 1/(l**2)
p2 = l**2
#print(v, p2)
def f(x, a, b):
    return a*x +b


params1, cov1 = curve_fit(f, p1, yw)
params2, cov2 = curve_fit(f, p2, yw)

covv1 = np.sqrt(np.diag(cov1))
covv2 = np.sqrt(np.diag(cov2))

par1=params1[1]
par2=params1[0]
par3=params2[1]
par4=params2[0]
t=np.linspace(400,700)
plt.plot(l, yw,'rx',label='Messwerte')
plt.plot(t, par1+par2/(t**2), label='Dispersionskurve 1')
plt.plot(t, par3+par4*t**2, label='Dispersionskurve 2')
#plt.plot(x,f(x, *params1), 'r-', label='Ausgleichsgerade' )
plt.grid()
plt.xlabel(r'$\lambda \: / \: nm$')
plt.ylabel(r'$n^2$')
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('plot2.pdf')
plt.show()
