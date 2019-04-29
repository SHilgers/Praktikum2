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

p1= 1/(l**2)
p2 = l**2
#print(v, p2)
def f(x, a, b):
    return a*x +b

yw= w**2
params1, cov1 = curve_fit(f, p1, yw)
params2, cov2 = curve_fit(f, p2, yw)

covv1 = np.sqrt(np.diag(cov1))
covv2 = np.sqrt(np.diag(cov2))

#print(params1[0],'pm',covv1[0], 'und b ist ',params1[1],'pm',covv1[1])
#print(params2[0],'pm',covv2[0], 'und b2 ist ',params2[1],'pm',covv2[1])
Ao=ufloat(params1[0], covv1[0])
Az=ufloat(params1[1], covv1[1])
lc = (Ao*1/656**2 + Az)**(1/2)
ld = (Ao*1/589**2 + Az)**(1/2)
lf = (Ao*1/486**2 + Az)**(1/2)
#print(lc, ld, lf)
ab = (ld-1)/(lf-lc)
#print(ab)

auf = 3.000000*10**7*(Ao)/((656.0**3)*(Az+Ao/(656.0**2))**(1/2))
auf2 = 3.000000*10**7*(Ao)/((589.0**3)*(Az+Ao/(589.0**2))**(1/2))
auf3 = 3.00000*10**7*(Ao)/((486.0**3)*(Az+Ao/(486.0**2))**(1/2))

print(auf, auf2, auf3)
sor = (params1[0]/(params1[1]-1))**(1/2)
#print(sor)
sn = []
k = 0
for k in range(0,8) :
    sn.append((yw[k]- params1[1]-params1[0]/l[k]**2)**2)
    k = k+1

ges = (1/6)*(sn[0]+sn[1]+sn[2]+sn[3]+sn[4]+sn[5]+sn[6]+sn[7])
#print(ges)

sn2 = []
k2 = 0
for k2 in range(0,8) :
    sn2.append((yw[k2]- params2[1]-params2[0]*l[k2]**2)**2)
    k2 = k2+1

ges2 = (1/6)*(sn2[0]+sn2[1]+sn2[2]+sn2[3]+sn2[4]+sn2[5]+sn2[6]+sn2[7])
#print(ges2)

l2 = (Ao/(Az-1))**(1/2)
print(l2)
