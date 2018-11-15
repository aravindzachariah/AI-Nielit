from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
def f(x,y):
	return np.sin(np.sqrt(x**2+y**2))
x=np.linspace(-6,6,30)
y=np.linspace(-6,6,30)
X,Y=np.meshgrid(x,y)
z=f(X,Y)
fig=plt.figure()
ax=plt.axes(projection='3d')
ax.plot_surface(X,Y,z,rstride=1,cstride=1,cmap='viridis',edgecolor='none')
ax.set_title('surface')
