import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.DataFrame({'sample':
    [
        "PSNR"
    ],
    'ST-cGAN':
        [29.1763],
    'Pix2Pix GAN':
        [23.4428],
    'ResUNet':
        [22.8998],
    'TransFuse':
        [26.0847],
    'TransUNet':
        [27.4720],
    'U-Transformer':
        [26.1490],
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
            alpha=0.1,
            )
plt.legend(bbox_to_anchor=(1.0, 1.1), fontsize=14)
# plt.legend(loc='upper right', edgecolor='blue')
# 设置标题
# plt.title('F-actin')

# 设置刻度标签的角度和位置
ax.set_rgrids([20.0, 21.0, 22, 23, 24, 25, 26, 27, 28, 29, 30],
              color="grey",
              size=11,
              angle=90)
plt.ylim(20, 30)
plt.savefig('nuclei_radar_psnr.png')
plt.show()
