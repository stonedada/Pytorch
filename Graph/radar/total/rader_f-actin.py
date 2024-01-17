import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.DataFrame({'sample':
                         ["MAE",
                          "NRMSE",
                          "SSIM",
                          "PCC",
                          "R2",
                          ],
                     'STNet':
                         [0.2333, 0.3051, 0.8829, 0.9411, 0.8787],
                     'ResUNet':
                         [0.4242, 0.5493, 0.6867, 0.7842, 0.6034],
                     'TransFuse':
                         [0.3266, 0.4494, 0.7912, 0.8608, 0.7332],
                     'TransUNet':
                         [0.2479, 0.3190, 0.8529, 0.9307, 0.8639],
                     'UTransformer':
                         [0.2791, 0.3034, 0.8593, 0.9410, 0.8778],
                     })

plt.figure(figsize=(9, 8))
# 设置雷达图的参数
params = {
    'figure.figsize': [6, 6],
    'axes.labelsize': 14,
    'axes.titlesize': 16,
    'xtick.labelsize': 10,
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
            # 'y',     # color
            linewidth=2,  # line width
            linestyle='solid',
            label=data['sample'][i],
            )

    ax.fill(angles, values[i],
            'b',
            alpha=0.01,
            )
plt.legend(bbox_to_anchor=(1.2, 1.1), fontsize=14)
# plt.legend(loc='upper right', edgecolor='blue')
# 设置标题
plt.title('F-actin')

# 设置刻度标签的角度和位置
ax.set_rgrids([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1],
              color="grey",
              size=11,
              angle=90)
plt.ylim(0, 1)
plt.savefig('f-actin_radar.png')
plt.show()
