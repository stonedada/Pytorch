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
                         [0.1496, 0.2980, 0.7784, 0.9464, 0.8800],
                     'ResUNet':
                         [0.2872, 0.6120, 0.5402, 0.7402, 0.5043],
                     'TransFuse':
                         [0.2001, 0.4326, 0.6520, 0.8751, 0.7439],
                     'TransUNet':
                         [0.1991, 0.4099, 0.6481, 0.8909, 0.7772],
                     'UTransformer':
                         [0.1760, 0.2957, 0.7960, 0.9471, 0.8844],
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
            # 'y',                        # color
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
plt.title('Nuclei')

# 设置刻度标签的角度和位置
ax.set_rgrids([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1],
              color="grey",
              size=11,
              angle=90)
plt.ylim(0, 1)
plt.savefig('nuclei_radar.png')
plt.show()
