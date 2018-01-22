import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.stats import sem

a=[1.16, 0.98, 1.10, 1.04, 1.13, 1.06, 1.32, 1.20, 1.32, 1.20, 1.28]
b=[0.67, 0.62, 0.72, 0.75, 0.64, 0.79, 0.93, 0.64, 0.72, 0.67, 0.67, 0.93]
c=[1.93, 2.04,2.16, 1.97, 2.12, 2.14, 2.10, 2.14, 1.98, 2.12]
t=[3, 2, 3, 3, 3, 4, 3, 3, 3, 2, 1, 2]

d=sum(a) / float(len(a))
e=sum(b) / float(len(b))
f=sum(c) / float(len(c))
s=sem(t)

print(d)
print(e)
print(f)
print(s)
#g=sum((0.67-e)^2+(0.62-e)^2+(0.72-e)^2+(0.75-e)^2+(0.64-e)^2+(0.79-e)^2+(0.93-e)^2+(0.64-e)^2+(0.72-e)^2+2(0.67-e)^2+(0.93-e)^2)
#x = \frac{1}{N}\sqrt{\frac{1}{N-1}\cdot\sum_{1}^N (x_{i}-\bar x)^2}
#print(g)
