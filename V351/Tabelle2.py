import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

a = np.genfromtxt('SpannungDreieck.txt', unpack=True)
b = 2.66

c=a/b
print(c)
