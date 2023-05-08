import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.DataFrame({'sample':
                         ["MAE",
                          "NRMSE",
                          "SSIM",
                          "PCC",
                          "Dice",
                          "IoU",
                          "R2",
                          ],
                     'F-actin_microDL':
                         [0.2915, 0.4079, 0.7870, 0.7960, 0.98929, 0.0809, 0.5743],
                     'Nuclei_microDL':
                         [0.4836, 0.6836, 0.7130, 0.6581, 0.9800, 0.0139, 0.4072],
                     'F-actin_ResUNet':
                         [0.4242, 0.5493, 0.6867, 0.7842, 0.9720, 0.2623, 0.6034],
                     'Nuclei_ResUNet':
                         [0.2872, 0.6120, 0.5402, 0.7402, 0.9716, 0.1115, 0.5043],
                     'F-actin_TransFuse':
                         [0.3233, 0.4494, 0.7912, 0.8608, 0.9730, 0.3012, 0.7332],
                     'Nuclei_TransFuse':
                         [0.2001, 0.4326, 0.6520, 0.8751, 0.9686, 0.2041, 0.7439],
                     'F-actin_TransUNet':
                         [0.2479, 0.3190, 0.8529, 0.9307, 0.9812, 0.3564, 0.8639],
                     'Nuclei_TransUNet':
                         [0.1991, 0.4099, 0.6481, 0.8909, 0.9798, 0.2718, 0.7772],
                     'F-actin_UTransform':
                         [0.2492, 0.3034, 0.8593, 0.9410, 0.9837, 0.4840, 0.8778],
                     'Nuclei_UTransform':
                         [0.1450, 0.2957, 0.7960, 0.9471, 0.9863, 0.5022, 0.8844],
                     })

plt.figure(figsize=(12, 8))
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

plt.legend(bbox_to_anchor=(0.8, 0.78), fontsize=14)
# plt.title('Radar Chart of Three Indicators for Five Samples')

# 设置刻度标签的角度和位置
ax.set_rgrids([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1],
              color="grey",
              size=11,
              angle=90)
plt.ylim(0, 1)
plt.savefig('total_radar.png')
plt.show()
