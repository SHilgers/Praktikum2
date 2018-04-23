import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.stats import sem

b=0.00015
s=0.001 #Hersteller
b2 =ufloat(2.474726849281404e-10,0.013631278926860252)
s2 =ufloat(0.024905557750864383,4.466162820933338e-05)
b3= (b2-b)/b
print(b3) #Abweichung
s3=(s2-s)/s
print(s3) #Abweichung

B=0.0001
S=0.004
B2 =ufloat(3.1484052675656174e-05,9.210238372573248e-07)
S2 =ufloat(0.024699091412915715,0.0001467769454825804)
B3= (B2-B)/B
print(B3) #Abweichung
S3=(S2-S)/S
print(S3) #Abweichung

e=0.00015
e2=ufloat(0.0001508531563845671,4.153627304462559e-06)
e3= (e2-e)/e
print(e3) #Abweichung
