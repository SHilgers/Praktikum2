import numpy as np
from numpy import exp
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.stats import sem

x, y= np.genfromtxt('Werte1.txt', unpack=True)
x1, y1= np.genfromtxt('Werte1a.txt', unpack=True)
x2, y2= np.genfromtxt('Werte1b.txt', unpack=True)
Nu=215 #215 auf 900s
Nun=(215/900)*10
x=x*10
x1=x1*10
x2=x2*10
yln=np.log(y-Nun)
y1=np.log(y1-Nun)
y2=np.log(y2-Nun)

def f(x, a, b):
    return a*x+b
params, cov = curve_fit(f, x1, y1)
errors = np.sqrt(np.diag(cov))
print('a =', params[0], '±', errors[0])
print('b =', params[1], '±', errors[1])
a=ufloat(params[0], errors[0])
b=ufloat(params[1], errors[1])

def g(x, c, d):
    return c*x+d
params2, cov2 = curve_fit(g, x2, y2)
errors2 = np.sqrt(np.diag(cov2))
print('c =', params2[0], '±', errors2[0])
print('d =', params2[1], '±', errors2[1])
c=ufloat(params2[0], errors2[0])
d=ufloat(params2[1], errors2[1])

def h(x):
    return (params[0]-params2[0])*x+(params[1]-params2[1])
    #(a-c)x +b-d
ak=a-c
bk=b-d
print('ak,steigung kurzlebig=',ak, 'bk, y-Achsenabschnitt', bk)


#Geradengleichungen, werte bei t*=200s
Nkt=ak*200+bk
print('N_kurz_t*=', Nkt)
Nlt= c*200 +d
print('N_lang_t*=', Nlt)
#Halbwertszeiten:T=ln(2)/lambda
Tl=np.log(2)/c
Tk=np.log(2)/ak
Tges=np.log(2)/a
print('Tlang=', Tl, 'Tkurz=',Tk, 'Tges=', Tges)
#N0(1-e....)
Nk=2.718**bk
Nl=2.718**d
Nges=2.718**b
print('Nk=', Nk, 'Nl=', Nl, 'Nges=',Nges)

#wirklich N0=e^b/(1-e^(-lambda*t))
N0k=Nk/(1-np.exp(-(params[0]-params2[0])*y))
N0l=Nl/(1-np.exp(-params2[0])*y)
N0kmean=np.mean(N0k)
N0lmean=np.mean(N0l)
print('N0k=',N0kmean, 'N0l=', N0lmean)

t=np.linspace(0, 240)
u=np.linspace(240, 440)
ges=np.linspace(0, 440)

plt.plot (x, yln, 'rx', label='Messwerte')
plt.axvline(x=240)
plt.plot(t,f(t, *params), 'b-' ,label='Ausgleichsgerade gesamt ')
plt.plot(u,g(u, *params2), 'c-' ,label='Ausgleichsgrade langlebiges Isotop')
plt.plot(t,h(t), 'g--', label='Ausgleichsgerade kurzlebiges Isotop')
#plt.yscale('log')
plt.xlabel(r'$ t/s$')
plt.ylabel(r'$ ln(N)$')
plt.tight_layout()
plt.legend()
plt.savefig('plot1.pdf')
plt.show()
