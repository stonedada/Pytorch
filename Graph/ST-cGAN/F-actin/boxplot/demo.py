import matplotlib.pyplot as plt
import numpy as np

# 创建示例数据
data1 = np.random.normal(0, 1, 100)
data2 = np.random.normal(0, 10, 100)

# 绘制第一组箱线图
fig, ax1 = plt.subplots()
ax1.boxplot(data1, vert=False)
ax1.set_yticks([1])
ax1.set_yticklabels(['Left Ylabel'])
ax1.set_ylabel('Overall Ylabel')

# 创建次坐标轴并绘制第二组箱线图
ax2 = ax1.twinx()
ax2.boxplot(data2, vert=False, positions=[2])
ax2.set_yticks([2])
ax2.set_yticklabels(['Right Ylabel'])
ax2.set_ylabel('')

# 显示图形
plt.show()
