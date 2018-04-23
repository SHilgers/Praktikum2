import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat

x,y = np.genfromtxt('Werte3.txt', unpack=True)

y=y*10**(-9)-0.1*10**(-9) #y=gemessener Strom
x=x/1000 #position von Detektor
l=635*10**(-9) #Wellenlänge
L=1.085 #Abstand Spalt-Schirm
#m= x0, theoretischer Mittelpunkt


#def f(x, b, m):
#    return 1*b**(2)*np.sinc((b*np.sin((x-m)/L))/l)
def f(x, b, m):
    return 1.65*b**(2)*(l/(np.pi*b*np.sin((x-m)/L)))**(2)*np.sin((np.pi*b*np.sin(x-m)/L)/l)**(2)


params, cov = curve_fit(f, x, y, p0=(0.00015, 0.02475 ))
#, p0=(0.25, 0.0008, 0.001)
errors = np.sqrt(np.diag(cov))
#p0=(0.025, 0.000000008, 1)
print('b =', params[0], '±', errors[0])
print('m =', params[1], '±', errors[1])



t=np.linspace(0.015, 0.036, 10000)
plt.plot (x , y, 'rx', label='Messwerte')
plt.plot(t, f(t, *params), 'b-' ,label='Ausgleichsfunktion f(x)')
plt.xlabel(r'x in mm')
plt.ylabel(r'Intensität I in nA')
plt.legend()
plt.tight_layout()
plt.show()
plt.savefig('plot4.pdf')
