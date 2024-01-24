import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def normalize_list(input_list, new_min=0, new_max=1):
    """
    将输入列表归一化到指定的范围 [new_min, new_max]。

    参数：
    - input_list: 要归一化的输入列表
    - new_min: 新的最小值
    - new_max: 新的最大值

    返回：
    - 归一化后的列表
    """
    old_min = min(input_list)
    old_max = max(input_list)

    normalized_list = [(x - old_min) / (old_max - old_min) * (new_max - new_min) + new_min for x in input_list]

    return normalized_list


# 读取数据
data = pd.read_csv('data/Gt_Values.csv')
col1_title = 'Distance_(pixels)'
col2_title = 'Gray_Value'
col1_data = data[col1_title]
col2_data = data[col2_title]
x = normalize_list(col1_data.tolist())
y = normalize_list(col2_data.tolist())

# 构建画布
plt.figure(figsize=(10, 5))
plt.plot(x, y, label='Ground truth', linewidth=5, color='#ff7f0e')

# 显示图例，并设置标签字体大小
plt.legend(fontsize=15)

plt.xlabel('Distance (pixels)', fontsize=20)
plt.ylabel('Gray Value', fontsize=20)
dest = './Gt.png'
plt.savefig(dest)

plt.show()
