import numpy as np

xx = np.linspace(-0.80,0.80,64)
yy = xx.copy()

X, Y = np.meshgrid(xx, yy)

nx, ny = 20, 20

x = np.linspace(-0.80,0.80,nx)

y = np.linspace(-0.80,0.80,ny)

X1, Y1 = np.meshgrid(xx, yy)