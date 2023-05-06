import matplotlib.pyplot as plt
import numpy as np

all_data = [np.random.normal(0, std, 100) for std in range(1, 4)]
# print(all_data)
font_size = 15
# ----------多个子图-----------
figure, axes = plt.subplots(1, 3)  # 得到画板、轴
axes = axes.flatten()
figure.set_size_inches(15, 6)
a = axes[0].boxplot(all_data, patch_artist=True, )  # 描点上色
axes[0].set_title('F-actin', fontsize=font_size)
b = axes[1].boxplot(all_data, patch_artist=True, )  # 描点上色
axes[1].set_title('Nuclei', fontsize=font_size)
c = axes[2].boxplot(all_data, patch_artist=True, )  # 描点上色

# 颜色填充
colors = ['pink', 'lightblue', 'lightgreen']
for bplot in (a, b, c):
    for patch, color in zip(bplot['boxes'], colors):
        patch.set_facecolor(color)
# 加水平网格线
for ax in axes:
    ax.yaxis.grid(True)  # 在y轴上添加网格线
    ax.xaxis.grid(True)  # 在x轴上添加网格线
    ax.set_xticks([y + 1 for y in range(len(all_data))])  # 指定x轴的轴刻度个数
    ax.set_xlabel('Model')  # 设置x轴名称
    ax.set_ylabel('Dice')  # 设置y轴名称

plt.setp(axes, xticks=[1, 2, 3], xticklabels=['TransUNet', 'TransFuse', 'UTransform'])

# ----------单个图-----------
# plt.figure(figsize=(10,5))
# plt.title('accuracy')
# plt.boxplot(all_data, labels=['haha','sas','hh'],patch_artist=True)
# plt.xlabel('model')
# plt.ylabel('Dice')
plt.show()  # 展示
