"""
http://c.biancheng.net/matplotlib/subplot.html
Matplotlib subplot()函数用法详解

在使用 Matplotlib 绘图时，我们大多数情况下，需要将一张画布划分为若干个子区域，之后，我们就可以在这些区域上绘制不用的图形。在本节，我们将学习如何在同一画布上绘制多个子图。

matplotlib.pyplot模块提供了一个 subplot() 函数，它可以均等地划分画布，该函数的参数格式如下：

plt.subplot(nrows, ncols, index)
nrows 与 ncols 表示要划分几行几列的子区域（nrows*nclos表示子图数量），index 的初始值为1，用来选定具体的某个子区域。

例如： subplot(233)表示在当前画布的右上角创建一个两行三列的绘图区域（如下图所示），同时，选择在第 3 个位置绘制子图。
"""
import matplotlib
print(matplotlib.get_backend())
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import numpy as np
import math
x = np.arange(0, math.pi*2, 0.05)
print('x=', x, ' len=', len(x))
fig=plt.figure()
axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # main axes
axes2 = fig.add_axes([0.55, 0.55, 0.3, 0.3]) # inset axes
y = np.sin(x)
axes1.plot(x, y, 'b')
axes2.plot(x,np.cos(x),'r')
axes1.set_title('sine')
axes2.set_title("cosine")
plt.show()