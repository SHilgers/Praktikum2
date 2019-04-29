import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat

x,y = np.genfromtxt('Werte3a.txt', unpack=True)
X,Y = np.genfromtxt('Werte3b.txt', unpack=True)
y=y*10**(-9)-0.1*10**(-9) #y=gemessener Strom
x=x/1000 #position von Detektor
Y=Y*10**(-9)-0.1*10**(-9) #y=gemessener Strom
X=X/1000 #position von Detektor
l=635*10**(-9) #Wellenlänge
L=1.085 #Abstand Spalt-Schirm
#m= x0, theoretischer Mittelpunkt


def f(x,i, b, m):
    return i*b**(2)*np.sinc((b*np.sin((x-m)/L))/l)
#def f(x,i, b, m):
#    return i*b**(2)*(l/(np.pi*b*np.sin((x-m)/L)))**(2)*np.sin((np.pi*b*np.sin(x-m)/L)/l)**(2)


params, cov = curve_fit(f, x, y, p0=(4, 0.00015, 0.025 ))
#, p0=(0.25, 0.0008, 0.001)
errors = np.sqrt(np.diag(cov))
#p0=(0.025, 0.000000008, 1)
print('i =', params[0], '±', errors[0])
print('b =', params[1], '±', errors[1])
print('m =', params[2], '±', errors[2])

def g(X,I, B, M):
    return I*B**(2)*np.sinc((B*np.sin((X-M)/L))/l)
#def g(X,I, B, M):
#    return I*B**(2)*(l/(np.pi*B*np.sin((X-M)/L)))**(2)*np.sin((np.pi*B*np.sin(X-M)/L)/l)**(2)


params2, cov2 = curve_fit(g, X, Y, p0=(4 ,0.00015, 0.025 ))
#, p0=(0.25, 0.0008, 0.001)
errors2 = np.sqrt(np.diag(cov2))
#p0=(0.025, 0.000000008, 1)
print('I =', params[0], '±', errors[0])
print('B =', params[1], '±', errors[1])
print('M =', params[2], '±', errors[2])


t=np.linspace(0.015, 0.025, 10000)
u=np.linspace(0.025, 0.036, 10000)
plt.plot (x , y, 'rx', label='Messwerte')
plt.plot (X , Y, 'rx')
plt.plot(t, f(t, *params), 'b-' ,label='Ausgleichsfunktion f(x)')
plt.plot(u, g(u, *params2), 'g--' ,label='Ausgleichsfunktion g(x)')
plt.xlabel(r'x in mm')
plt.ylabel(r'Intensität I in nA')
plt.legend()
plt.tight_layout()
plt.show()
plt.savefig('plot4.pdf')
