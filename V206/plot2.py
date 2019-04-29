import numpy as np
from numpy import exp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat
t, a, b, c, d, p= np.genfromtxt('Werte.txt', unpack=True)

def f(t, l, m, n):
    return l*t**2 + m*t + n

params, cov = curve_fit(f, t, c)

errors = np.sqrt(np.diag(cov))

print('l =', params[0], '±', errors[0])
print('m =', params[1], '±', errors[1])
print('n =', params[2], '±', errors[2])

parrams, covv = curve_fit(f, t, d)

errrors = np.sqrt(np.diag(covv))

print('lk =', parrams[0], '±', errrors[0])
print('mk =', parrams[1], '±', errrors[1])
print('nk =', parrams[2], '±', errrors[2])

lw=ufloat(params[0], errors[0])
lk=ufloat(parrams[0], errrors[0])
mw=ufloat(params[1], errors[1])
mk=ufloat(parrams[1], errrors[1])

dw1 = lw*480 + mw
dw2 = lw*960 + mw
dw3 = lw*1500 + mw
dw4 = lw*1980 + mw

dk1 = lk*480 + mk
dk2 = lk*960 + mk
dk3 = lk*1500 + mk
dk4 = lk*1980 + mk

print ('dw= ', dw1, dw2, dw3, dw4)
print ('dk= ', dk1, dk2, dk3, dk4)

w= 4*4183
q= 750
v1= dw1 * (w+q)*1/(122)
v2= dw2 * (w+q)*1/(122)
v3= dw3 * (w+q)*1/(124)
v4= dw4 * (w+q)*1/(125)
print('v1= ', v1, 'v2= ', v2, 'v3= ', v3, 'v4= ', v4)

vt1= (29.2+273.15)/(29.2-14.5)
vt2= (37.4+273.15)/(37.4-9.4)
vt3= (44.4+273.15)/(44.4-5.6)
vt4= (49.3+273.15)/(49.3-3.8)
print('vt1= ', vt1, 'vt2= ', vt2, 'vt3= ', vt3, 'vt4= ', vt4)

ab1 = (vt1-v1)/vt1
ab2 = (vt2-v2)/vt2
ab3 = (vt3-v3)/vt3
ab4 = (vt4-v4)/vt4
print('ab1= ', ab1, 'ab2= ', ab2, 'ab3= ', ab3, 'ab4= ', ab4)
l= ufloat(19462, 575)
dm1= ((dk1*(w+q) )/l)*120.91
dm2= ((dk2*(w+q) )/l)*120.91
dm3= ((dk3*(w+q) )/l)*120.91
dm4= ((dk4*(w+q) )/l)*120.91

print('dm1= ', dm1, 'dm2= ', dm2, 'dm3= ', dm3, 'dm4= ', dm4)

pa1=4.3
pa2=3.8
pa3=3.6
pa4=3.5
pb1=7.8
pb2=9.2
pb3=11.0
pb4=12.1
k=1.14
p= 5.51
n1=(1/(k-1))*(pb1*((pa1/pb1)**(1/k))-pa1)*((14.5+273.15)*p/((273.15)*pa1))*dm1
n2=(1/(k-1))*(pb2*((pa2/pb2)**(1/k))-pa2)*((9.4+273.15)*p/((273.15)*pa2))*dm2
n3=(1/(k-1))*(pb3*((pa3/pb3)**(1/k))-pa3)*((5.6+273.15)*p/((273.15)*pa3))*dm3
n4=(1/(k-1))*(pb4*((pa4/pb4)**(1/k))-pa4)*((3.8+273.15)*p/((273.15)*pa4))*dm4

print('n1= ', n1, 'n2= ', n2, 'n3= ', n3, 'n4= ', n4)

x=np.linspace(0, 2000)
#plt.xscale('log')
plt.plot (t, c, 'rx', label='$T_1$')
plt.plot (t, d, 'bx', label='$T_2$')
plt.plot(x,f(x, *params), 'r-' ,label='Ausgleichsfunktion von $T_1$')
plt.plot(x,f(x, *parrams), 'b-' ,label='Ausgleichsfunktion von $T_2$')
plt.xlabel(r'$t \: /\: s$')
plt.ylabel(r'$ T \: / \: °C $')
plt.legend(loc="best")
plt.tight_layout()
plt.savefig('plot1.pdf')
plt.show()
