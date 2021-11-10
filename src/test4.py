"""
http://c.biancheng.net/matplotlib/axes.html
Matplotlib axes类使用详解

Matplotlib 定义了一个 axes 类（轴域类），该类的对象被称为 axes 对象（即轴域对象），它指定了一个有数值范围限制的绘图区域。
在一个给定的画布（figure）中可以包含多个 axes 对象，但是同一个 axes 对象只能在一个画布中使用。
2D 绘图区域（axes）包含两个轴（axis）对象；如果是 3D 绘图区域，则包含三个。
"""
import matplotlib
print(matplotlib.get_backend())
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt

y = [1, 4, 9, 16, 25,36,49, 64]
x1 = [1, 16, 30, 42,55, 68, 77,88]
x2 = [1,6,12,18,28, 40, 52, 65]
fig = plt.figure()

# add_axes() 的参数值是一个序列，序列中的 4 个数字分别对应图形的左侧，底部，宽度，和高度，且每个数字必须介于 0 到 1 之间。
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

#使用简写的形式color/标记符/线型
l1 = ax.plot(x1,y,'ys-') 
l2 = ax.plot(x2,y,'go--') 
ax.legend(labels = ('tv', 'Smartphone'), loc = 'lower right') # legend placed at lower right
ax.set_title("Advertisement effect on sales")
ax.set_xlabel('medium')
ax.set_ylabel('sales')
plt.show()