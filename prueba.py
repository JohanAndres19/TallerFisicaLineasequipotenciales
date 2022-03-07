
#%%
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle
from numpy.lib.type_check import real

# # puntos de los ejes x , y.

xx = np.linspace(-0.80,0.80,64)
yy = xx.copy()

X, Y = np.meshgrid(xx, yy)


#funcion potencial elentrico en terminos de  X y Y
V=(9*10**9)*(30*10**(-9))*np.log((((X+0.3)**2+Y**2)**0.5+X+0.3)/((X**2+Y**2)**0.5+X))

#Generar grafica
figura = plt.figure()
ax =figura.add_subplot(111)

# # Agregar rectangulo como distrubucion continua de carga.
charge_colors = {True: '#aa0000', False: '#0000aa'}
ax.add_patch(Rectangle((-0.3,-0.0125),0.30,0.02,color=charge_colors[1>0],fill=True))

#Graficar
ax.set_xlabel('$x(m)$')
ax.set_ylabel('$y(m)$')
ax.set_xlim(-0.60,0.40,)
ax.set_ylim(-0.5,0.5)
ax.grid()

# Lineas equipotenciales
cs=ax.contour(X,Y,V)

#generar etiquetas de las graficas
ax.clabel(cs,inline=2,fontsize=6)

#Mostrar Grafica
plt.show()

