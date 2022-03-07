import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle
import sympy as sp

xx = np.linspace(-0.35,0.05)
yy = np.linspace(-0.35,0.35)
X,Y= np.meshgrid(xx, yy)

x=sp.symbols('x')

y=sp.symbols('y')

V=((9*10**9)*(30*10**(-9))*sp.log((sp.sqrt((x+0.3)**2+(y-0.05)**2)+x+0.3)/(sp.sqrt(x**2+(y-0.05)**2)+x)))+((9*10**9)*(-30*10**(-9))*sp.log((sp.sqrt((x+0.3)**2+(0.25-y)**2)+x+0.3)/(sp.sqrt(x**2+(0.25-y)**2)+x))) 

Pv=((9*10**9)*(30*10**(-9))*np.log((np.sqrt((X+0.3)**2+(Y-0.05)**2)+X+0.3)/(np.sqrt(X**2+(Y-0.05)**2)+X)))+((9*10**9)*(-30*10**(-9))*np.log((np.sqrt((X+0.3)**2+(0.25-Y)**2)+X+0.3)/(np.sqrt(X**2+(0.25-Y)**2)+X))) 


dvx=sp.sympify(-1*sp.diff(V,x))
dvy=sp.sympify(-1*sp.diff(V,y))

fdvx =sp.lambdify([x,y],dvx,"numpy")
fdvy =sp.lambdify([x,y],dvy,"numpy")

Ex=fdvx(X,Y)

Ey=fdvy(X,Y)


#Grafica
figura = plt.figure()

ax =figura.add_subplot(111)


color = 2 * np.log(np.hypot(Ex, Ey))

ax.streamplot(xx, yy, Ex, Ey, color=color, linewidth=1, cmap=plt.cm.inferno,

              density=2, arrowstyle='->', arrowsize=1.5)


charge_colors = {True: '#aa0000', False: '#0000aa'}

ax.add_patch(Rectangle((-0.303,0.040),0.30,0.01,color=charge_colors[1>0],fill=True))
ax.add_patch(Rectangle((-0.303,0.25),0.30,0.01,color=charge_colors[-1>0],fill=True))

ax.set_xlabel('$x(m)$')
ax.set_ylabel('$y(m)$')
ax.set_xlim(-0.40,0.10,)
ax.set_ylim(-0.10,0.40)
ax.grid()
ax.set_aspect('equal')

# Lineas equipotenciales
ax.contour(X,Y,Pv)

#generar etiquetas de las graficas
#ax.clabel(cs,inline=2,fontsize=6)

plt.show()

# %%
