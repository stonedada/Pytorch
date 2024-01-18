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
# input
data_input = pd.read_csv('data/input_Values.csv')
col1_title = 'Distance_(pixels)'
col2_title = 'Gray_Value'
x_input = normalize_list(data_input[col1_title].tolist())
y_input = normalize_list(data_input[col2_title].tolist())

# Gt
data_gt = pd.read_csv('data/Gt_Values.csv')
x_gt = normalize_list(data_gt[col1_title].tolist())
y_gt = normalize_list(data_gt[col2_title].tolist())

# TransUNet
data_TU = pd.read_csv('data/TransUNet_Values.csv')
x_TU = normalize_list(data_TU[col1_title].tolist())
y_TU = normalize_list(data_TU[col2_title].tolist())

# 构建画布
plt.figure(figsize=(10, 5))
plt.plot(x_input, y_input, label='Input', linewidth=5)
plt.plot(x_gt, y_gt, label='Ground truth', linewidth=5)
plt.plot(x_TU, y_TU, label='TransUNet', linewidth=5)

# 显示图例，并设置标签字体大小
plt.legend(fontsize=15)

# plt.title('Plot Values', fontsize=25)
plt.xlabel('Distance (pixels)', fontsize=20)
plt.ylabel('Gray Value', fontsize=20)
dest = './TransUNet.png'
plt.savefig(dest)

plt.show()
