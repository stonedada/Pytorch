import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 生成示例数据
np.random.seed(10)
data = pd.DataFrame({
    'A': np.random.normal(0, 1, 100),
    'B': np.random.normal(-2, 1, 100),
    'C': np.random.normal(2, 1, 100),
    'D': np.random.normal(0, 2, 100),
    'E': np.random.normal(-2, 2, 100)
})

# 设置绘图风格
sns.set(style="whitegrid")

# 创建一个2行3列的子图布局
fig, axs = plt.subplots(2, 3, figsize=(15, 10))

# 第一行绘制三个小提琴图
for i in range(3):
    sns.violinplot(y=data.iloc[:, i], ax=axs[0, i])

# 第二行绘制两个小提琴图
for i in range(3, 5):
    sns.violinplot(y=data.iloc[:, i], ax=axs[1, i - 3])

# 删除第二行第三列的空白子图
fig.delaxes(axs[1, 2])

plt.tight_layout()
plt.show()
