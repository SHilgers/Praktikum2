import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

a = np.genfromtxt('SpannungRechteck.txt', unpack=True)
b = 4.12

c=a/b
print(c)
