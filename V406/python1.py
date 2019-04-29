import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat

x,y = np.genfromtxt('Werte1b.txt', unpack=True)
X,Y = np.genfromtxt('Werte1a.txt', unpack=True)

y=y*10**(-1)-0.1*10**(-1) #y=gemessener Strom
x=x/1000 #position von Detektor
Y=Y*10**(-1)-0.1*10**(-1) #y=gemessener Strom
X=X/1000 #position von Detektor
l=635*10**(-9) #Wellenlänge
L=1.085 #Abstand Spalt-Schirm
#m= x0, theoretischer Mittelpunkt
phi=x/L
phi2=X/L
#def f(x, s, m, b):
#    return 8*np.cos(((np.pi*s*np.sin(x-m))/l))**(2)*np.sinc((b*np.sin(x-m))/l)**(2)
def f(X ,I, S, M, B):
    return I*np.cos(((np.pi*S*np.sin(X-M))/l))**(2)*np.sinc((B*np.sin(X-M))/l)**(2)


params, cov = curve_fit(f, X, Y,  p0=(8, 0.0001, 0.025, 0.00015))
errors = np.sqrt(np.diag(cov))
# p0=(0.0001, 0.025, 0.00015)
print('I =', params[0], '±', errors[0])
print('B =', params[1], '±', errors[1])
print('S =', params[2], '±', errors[2])
print('M =', params[3], '±', errors[3])

def g(x, i, s, m, b):
    return i*np.cos(((np.pi*s*np.sin(x-m))/l))**(2)*np.sinc((b*np.sin(x-m))/l)**(2)

params2, cov2 = curve_fit(g, x, y ,p0=(8, 0.0001, 0.025, 0.00015))
errors2 = np.sqrt(np.diag(cov2))
# p0=(8, 0.0001, 0.025, 0.00015)
#p0=(3, 0.001, 0.00025, 0.000015)
print('i =', params2[0], '±', errors2[0])
print('b =', params2[1], '±', errors2[1])
print('s =', params2[2], '±', errors2[2])
print('m =', params2[3], '±', errors2[3])


t=np.linspace(0.01, 0.025, 10000)
u=np.linspace(0.025, 0.04, 10000)
plt.plot (x , y, 'rx', label='Messwerte')
plt.plot (X, Y, 'rx', label='Messwerte')
plt.plot(t, f(t, *params), 'b-' ,label='Ausgleichsfunktion f(x)')
plt.plot(u, g(u, *params2), 'g--' ,label='Ausgleichsfunktion g(x)')
plt.xlabel(r'x in mm')
plt.ylabel(r'Intensität I in nA')
plt.legend()
plt.tight_layout()
plt.show()
plt.savefig('plot1.pdf')
