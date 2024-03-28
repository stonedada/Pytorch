import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.DataFrame({'sample':
                         [
                          "Dice",
                          ],
                     'F-actin_microDL':
                         [0.9829],
                     'Nuclei_microDL':
                         [0.9800],
                     'F-actin_ResUNet':
                         [0.9720],
                     'Nuclei_ResUNet':
                         [0.9716],
                     'F-actin_TransFuse':
                         [0.9730],
                     'Nuclei_TransFuse':
                         [0.9686],
                     'F-actin_TransUNet':
                         [0.9812],
                     'Nuclei_TransUNet':
                         [0.9798],
                     'F-actin_UTransform':
                         [0.9837],
                     'Nuclei_UTransform':
                         [0.9863],
                     })

plt.figure(figsize=(9, 8))
# 设置雷达图的参数
params = {
    'figure.figsize': [6, 6],
    'axes.labelsize': 14,
    'axes.titlesize': 16,
    'xtick.labelsize': 8,
    'ytick.labelsize': 10,
    'font.weight': 'bold'
}
plt.rcParams.update(params)

# 绘制雷达图
categories = list(data.columns[1:])
N = len(categories)
values = data.iloc[:, 1:].values.tolist()
angles = [n / float(N) * 2 * np.pi for n in range(N)]

# values每一行增加第一个数据; angle增加最后一个角度。 使得曲线闭合
_ = [value.append(value[0]) for value in values]
angles += angles[:1]

ax = plt.subplot(111, polar=True)
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)
plt.xticks(angles[:-1], categories)
ax.set_rlabel_position(0)

for i in range(len(values)):
    ax.plot(angles, values[i],
            # 'y',                        # color
            linewidth=2,  # line width
            linestyle='solid',
            label=data['sample'][i],
            )

    ax.fill(angles, values[i],
            'b',
            alpha=0.05,
            )

plt.legend(bbox_to_anchor=(0.9, 0.78), fontsize=14)
# plt.title('Radar Chart of Three Indicators for Five Samples')

# 设置刻度标签的角度和位置
ax.set_rgrids([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1],
              color="grey",
              size=11,
              angle=90)
plt.ylim(0, 1)
plt.savefig('total_radar_dice.png')
plt.show()
