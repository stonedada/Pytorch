import numpy as np
import matplotlib.pyplot as plt

# 创建一些示例数据
data = np.random.random((10, 10))

# 画热图
# plt.imshow(data, cmap='viridis', interpolation='nearest')
plt.imshow(data, cmap='coolwarm', interpolation='nearest')

# 添加颜色条
colorbar = plt.colorbar()

# 显示图形
plt.show()
