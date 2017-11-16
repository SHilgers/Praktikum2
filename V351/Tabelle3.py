import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

a = np.genfromtxt('SpannungSäge.txt', unpack=True)
b = 2.10

c=a/b
print(c)
