"""
http://c.biancheng.net/matplotlib/the-first-plot.html

第一个绘图程序
首先导入 Matplotlib 包中的 Pyplot 模块，并以 as 别名的形式简化引入包的名称。
接下来，使用 NumPy 提供的函数 arange() 创建一组数据来绘制图像。 
下面绘制一个简单正弦曲线图，它显示了角度与正弦函数值之间的关系。
"""

import matplotlib
print(matplotlib.get_backend())
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
import numpy as np
import math

#调用math.pi方法弧度转为角度
x = np.arange(0, math.pi*2, 0.05)
y1 = np.sin(x)
y2 = np.cos(x)
plt.plot(x,y1)
plt.plot(x,y2)
plt.xlabel("angle")
plt.ylabel("sine/cosine")
plt.title('sine/cosine wave')
#使用show展示图像
plt.show()