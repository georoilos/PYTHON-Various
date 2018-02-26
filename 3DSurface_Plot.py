import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

points = np.linspace(-1, 1, 101)
X, Y = np.meshgrid(points, points)
Z = X**2 + Y**2
ax = Axes3D(plt.figure())
ax.plot_surface(X, Y, Z, rstride=1, cstride=1)
plt.show()
