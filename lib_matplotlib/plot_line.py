import matplotlib
import matplotlib.pyplot as plt

import numpy as np

xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

plt.plot(xpoints, ypoints, label='linear')
plt.plot(xpoints, xpoints, 'o-', label='linear-dot')
plt.plot(ypoints, -ypoints, '--', label='dotted-line')
plt.plot(-ypoints, ypoints, 'o', label='dots-only')
plt.plot(-xpoints, ypoints, 'g^', label='green-triangle')
plt.plot(-xpoints, -xpoints, 'bs', label='red-squre')

plt.xlabel('X')
plt.ylabel('y')

# Add a legend
plt.legend()
plt.show()


import os
os.system('pause')