import matplotlib.pyplot as plt
import numpy as np

x, y = np.genfromtxt('werte4.txt', unpack=True)
a = y/12
#print (a)

b= np.log(a)
print (b)

z, c, d =np.genfromtxt('werte3.txt', unpack=True)
f = c/d * 2 * np.pi
#print (f)
