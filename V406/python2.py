import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat

x,y = np.genfromtxt('Werte2.txt', unpack=True)

y=y*10**(-9)-0.1*10**(-9) #y=gemessener Strom
x=x/1000 #position von Detektor
l=635*10**(-9) #Wellenlänge
L=1.085 #Abstand Spalt-Schirm
#m= x0, theoretischer Mittelpunkt

def f(x, s, m, b):
    return 4*np.cos((np.pi*s*np.sin((x-m)/L))/l)**(2)*(l/(np.pi*b*np.sin((x-m)/L)))**(2)*np.sin((np.pi*b*np.sin((x-m)/L))/l)**(2)
#def f(x, s, m, b):
#    return 4*np.cos(((np.pi*s*np.sin(x-m))/l))**(2)*np.sinc((b*np.sin(x-m))/l)**(2)
#def f(x, a, phi, b):
#    return (2*a*l)/(2*np.pi*np.sin(phi))*np.exp((2*np.j*b**np.pi*np.sin(phi))/2*l)*np.sin((2*b*np.pi*np.sin(phi))/(2*l))


params, cov = curve_fit(f, x, y, p0=(0.0001, 0.025 , 0.00015))
#, p0=(0.25, 0.0008, 0.001)
errors = np.sqrt(np.diag(cov))
#p0=(0.025, 0.000000008, 1)
print('b =', params[0], '±', errors[0])
print('s =', params[1], '±', errors[1])
print('m =', params[2], '±', errors[2])


t=np.linspace(0, 0.05, 10000)
plt.plot (x , y, 'rx', label='Messwerte')
plt.plot(t, f(t, *params), 'b-' ,label='Ausgleichsfunktion f(x)')
#plt.xlabel(r'$\text{Winkel}\;\frac{x}{L}$rad')
#plt.ylabel(r'Intensität $ I $')
plt.legend()
plt.tight_layout()
plt.show()
plt.savefig('plot2.pdf')
