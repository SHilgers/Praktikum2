import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat

x,y = np.genfromtxt('Werte1.txt', unpack=True)

y=y*10**(-9)-0.1*10**(-9) #y=gemessener Strom
x=x/1000 #position von Detektor
l=635*10**(-9) #Wellenlänge
L=1.085 #Abstand Spalt-Schirm
#m= x0, theoretischer Mittelpunkt

def f(x, s, m, b):
    return 8*np.cos((np.pi*s*np.sin((x-m)/L))/l)**(2)*(l/(np.pi*b*np.sin((x-m)/L)))**(2)*np.sin((np.pi*b*np.sin((x-m)/L))/l)**(2)
#normal faktor 4

params, cov = curve_fit(f, x, y,  p0=(0.0001, 0.025, 0.00015))
errors = np.sqrt(np.diag(cov))
# p0=(0.0001, 0.025, 0.00015)
print('b =', params[0], '±', errors[0])
print('s =', params[1], '±', errors[1])
print('m =', params[2], '±', errors[2])


t=np.linspace(-0.01, 0.04, 10000)
plt.plot (x , y, 'rx', label='Messwerte')
plt.plot(t, f(t, *params), 'b-' ,label='Ausgleichsfunktion f(x)')
#plt.xlabel(r'$\text{Winkel}\;\frac{x}{L}$rad')
#plt.ylabel(r'Intensität $ I $')
plt.legend()
plt.tight_layout()
plt.show()
plt.savefig('plot1.pdf')
