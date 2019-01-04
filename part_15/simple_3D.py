# -*- coding: cp936 -*-

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

#figsize:以英寸为单位的宽高，缺省值为 rc figure.figsize (1英寸等于2.54厘米)
fig=plt.figure(figsize=(16,12))
ax=Axes3D(fig)
#设置X,Y的值
#arange([start,] stop[, step,], dtype=None)根据start与stop指定的范围以及step设定的步长，生成一个 ndarray**: dtype
X=np.arange(-4,4,0.25)
Y=np.arange(-4,4,0.25)
X,Y=np.meshgrid(X,Y)
#设置高的值
R=np.sqrt(X**2+Y**2)
Z=np.sin(R)
#绘图，rstride,cstride设置横纵方向的密度程度，绘制颜色
ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap="rainbow")
#绘制投影等高线图，zdir按照哪个方向投，最终投影位置是多少，投影颜色是什么
ax.contourf(X,Y,Z,zdir='z',offset=1,cmap="rainbow")
ax.set_zlim=(-2,2)
plt.show()




