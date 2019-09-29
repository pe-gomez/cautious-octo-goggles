import matplotlib.pyplot as plt
import numpy as np

grade=[1, 2, 3 , 4, 5, 6, 7, 8, 9, 10]
weight_school1=[25, 30, 33, 36, 39, 42, 44, 48, 54, 60]
weight_school2=[27, 31, 36, 39, 44, 49, 58, 62, 63, 64]

plt.plot(grade, weight_school1)
plt.plot(grade, weight_school2)
plt.show()
