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
    'E': np.random.normal(-2, 2, 100),
    'F': np.random.normal(-2, 2, 100)
})

# 设置绘图风格
sns.set(style="whitegrid")

# 创建一个1x5的子图布局
fig, axs = plt.subplots(1, 6, figsize=(15, 6))   # 2x3 无法展平，即无法直接遍历

# 分别为每个子图绘制小提琴图，并设置纵坐标的刻度和标签
for i, ax in enumerate(axs):
    sns.violinplot(y=data.iloc[:, i], ax=axs[i])
    ax.set_yticks(np.linspace(data.iloc[:, i].min(), data.iloc[:, i].max(), 5))
    ax.set_ylabel(f'Label {data.columns[i]}')

plt.tight_layout()
plt.show()
