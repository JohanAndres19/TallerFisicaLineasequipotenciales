import numpy as np

import matplotlib.pyplot as plt

from matplotlib.patches import Circle, Rectangle



# # Función que retorna el campo Eléctrico.
def E(x, y):
    # valor negativo de la derivada parcial de la funcion voltaje con respecto a x 
    dvx =(-270*(-0.30*x**2-0.09*x+(-0.3*x-y**2-0.09)*((x**2+y**2)**0.5)+(-0.3*x+y**2)*((y**2+(x+0.3)**2)**0.5)+0.3*y**2-0.3*((x**2+y**2)**0.5)*((y**2+(x+0.3)**2)**0.5)))/((x+((y**2+(x+0.3)**2)**0.5)+0.3)*(x+((x**2+y**2)**0.5))*((x**2+y**2)**0.5)*((y**2+(x+0.3)**2)**0.5))
    # valor negativo de la derivada parcial de la funcion voltaje con respecto a y
    dvy =(-270*(x*y*(((x**2+y**2)**0.5)-0.6)+(-x*y-0.3*y)*((y**2+(x+0.3)**2)**0.5)-0.09*y))/((x+((y**2+(x+0.3)**2)**0.5)+0.3)*(x+((x**2+y**2)**0.5))*((x**2+y**2)**0.5)*((y**2+(x+0.3)**2)**0.5))
    return dvx, dvy


# # puntos de los ejes x , y.

nx, ny = 20, 20

x = np.linspace(-0.80,0.80,nx)

y = np.linspace(-0.80,0.80,ny)

X, Y = np.meshgrid(x, y)


#funcion potencial elentrico en terminos de  X y Y
V=(9*10**9)*(30*10**(-9))*np.log((((X+0.3)**2+Y**2)**0.5+X+0.3)/((X**2+Y**2)**0.5+X))


# # Vector de campo eléctrico como componentes separados (Ex,Ey)

Ex, Ey = np.zeros((ny, nx)), np.zeros((ny, nx))

# evaluar campo electrico en el conjunto de puntos X y Y
ex, ey = E(x=X, y=Y)
Ex += ex
Ey += ey
    
# generar Grafico

fig = plt.figure()

ax = fig.add_subplot(111)


# # Dibujar las líneas de flujo con mapa de colores y estilos apropiados.

color = 2 * np.log(np.hypot(Ex, Ey))

ax.streamplot(x, y, Ex, Ey, color=color, linewidth=1, cmap=plt.cm.inferno,

              density=2, arrowstyle='->', arrowsize=1.5)




# # Agregar rectangulo como distrubucion continua de carga.

charge_colors = {True: '#aa0000', False: '#0000aa'}
ax.add_patch(Rectangle((-0.3,-0.0125),0.30,0.03,color=charge_colors[1>0],fill=True))


# # Graficar

ax.set_xlabel('$x(m)$')

ax.set_ylabel('$y(m)$')

ax.set_xlim(-0.8,0.6)

ax.set_ylim(-0.85,0.85)


# lineas equipotenciales
ax.contour(X,Y,V)

#mostra grafica
plt.show()




